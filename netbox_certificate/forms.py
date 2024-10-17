from netbox.forms import NetBoxModelForm
from dcim.models import Device
from django.utils.translation import gettext as _
from utilities.forms.fields import CommentField, DynamicModelMultipleChoiceField
from django import forms

from .models import Certificate
from .validator import CertificateValidator

class CertificateForm(NetBoxModelForm):

    cert = forms.FileField(required=False,validators=[CertificateValidator()])
    comments = CommentField()

    hostname = DynamicModelMultipleChoiceField(
        label=_('Hostname'),
        required=False,
        queryset=Hostname.objects.all()
    )

    class Meta:
        model = Certificate
        fields = ('name', 'url', 'cert', 'comments', 'device', 'alert')

class CAForm(NetBoxModelForm):
    name = forms.CharField()

class HostnameForm(NetBoxModelForm):
    name = forms.CharField()
