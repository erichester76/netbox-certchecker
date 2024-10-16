from netbox.forms import NetBoxModelForm
from . import models
from django.utils.translation import gettext as _
from utilities.forms.fields import CommentField, DynamicModelMultipleChoiceField
from django import forms

from .models import Certificate
from .validator import CertificateValidator

class CertificateForm(NetBoxModelForm):

    cert = forms.FileField(required=False,validators=[CertificateValidator()])
    comments = CommentField()

    class Meta:
        model = models.Certificate
        fields = ('name', 'hostname', 'tenant', 'cert', 'ca', 'expiration_date', 'comments', 'alert')

class CAForm(NetBoxModelForm):
    name = forms.CharField()
    
    class Meta:
        model = models.CA
        fields = ('name', 'amce')


class HostnameForm(NetBoxModelForm):
    name = forms.CharField()
    
    class Meta:
        model = models.Hostname
        fields = ('name', 'ipaddress')
