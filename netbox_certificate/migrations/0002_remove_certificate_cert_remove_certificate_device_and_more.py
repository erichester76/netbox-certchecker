# Generated by Django 5.0.9 on 2024-10-16 23:27

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0121_customfield_related_object_filter'),
        ('ipam', '0070_vlangroup_vlan_id_ranges'),
        ('netbox_certificate', '0001_initial'),
        ('tenancy', '0015_contactassignment_rename_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='cert',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='device',
        ),
        migrations.AddField(
            model_name='certificate',
            name='cert_file',
            field=models.FileField(blank=True, null=True, upload_to='netbox_certificate/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='expiration_date',
            field=models.DateField(default='01/01/24'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tenancy.tenant'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='alert',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='CA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField()),
                ('amce', models.BooleanField(default=False)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='certificate',
            name='ca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='netbox_certificate.ca'),
        ),
        migrations.CreateModel(
            name='Hostname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField()),
                ('ipaddress', models.ManyToManyField(blank=True, to='ipam.ipaddress')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='certificate',
            name='hostname',
            field=models.ManyToManyField(blank=True, to='netbox_certificate.hostname'),
        ),
    ]