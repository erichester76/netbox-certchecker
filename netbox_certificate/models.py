from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse


class Hostname(NetBoxModel):
    name = models.CharField(        
        max_length=254,
        help_text='FQDN',
        verbose_name='FQDN',

    )
    ipaddress = models.ManyToManyField(
        to='ipam.ipaddress',
        verbose_name='IP Address',
        help_text='IP of Hostname',
        blank=True
    )
    
    class Meta:
        verbose_name = ('Hostname')
        verbose_name_plural = ('Hostnames')
        ordering = ("name",)
        
    def get_absolute_url(self):
        return reverse('plugins:netbox_certificate:hostname', args=[self.pk])

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class CA(NetBoxModel):
    name = models.CharField(
        max_length=254,
        help_text='Certificate Authority',
    )
    amce = models.BooleanField(
        default=False,
        verbose_name='ACME Managed',
        help_text='Is Certificate managed by ACME',
    )
    
    class Meta:
        verbose_name = ('Certificate Authority')
        verbose_name_plural = ('Certificate Authorities')
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_certificate:ca", args=[self.pk])
    
    def delete(self, *args, **kwargs):

        super().delete(*args, **kwargs)

class Certificate(NetBoxModel):
    name = models.CharField(
        max_length=254,
        help_text='Certificate Name',
    )
    
    tenant = models.ForeignKey(
        to='tenancy.tenant', 
        on_delete=models.PROTECT,
        default=1
    )
    
    url = models.URLField(
        max_length=1024,
        help_text='Certificate and associated URL. Use the check tool to periodically access HTTPS and check the expiration date of the certificate.'
    )
    
    comments = models.TextField(
        blank=True,
    )
    
    hostname = models.ManyToManyField(
        to=Hostname,
        verbose_name='Hostname',
        help_text='Hostname with certificate installed',
        blank=True
    )
    
    ca = models.ForeignKey(
        to=CA, 
        on_delete=models.PROTECT,
        help_text='Certicate Authority',
        verbose_name='Certicate Authority',
        null=True, 
        blank=True
    )
    
    cert_file = models.FileField(
        upload_to='netbox_certificate/%Y/%m/%d/',
        verbose_name='Certificate File',
        help_text='You can upload your certificate file. This file is not used for monitoring.',
        null=True, 
        blank=True
    )
    expiration_date = models.DateField(
        verbose_name="Expiration Date",
        help_text="Expiration Date",
        default="2024-01-01"
    )
    alert = models.BooleanField(
        default=True,
        help_text='Controls enable/disable of alerts. It can also be used to temporarily stop alerts.'
    )
    

    def get_absolute_url(self):
        return reverse('plugins:netbox_certificate:certificate', args=[self.pk])

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):

        super().delete(*args, **kwargs)

        # Delete file from disk
        self.cert_file.delete(save=False)

