from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from .. import models

class CertificateSerializer(NetBoxModelSerializer):

    class Meta:
        model = models.Certificate
        fields = ( 'id', 'name', 'url', 'cert', 'ca', 'hostname', 'alert', 'comments', 'tags', 'custom_fields', 'created', 'last_updated')

class CASerializer(NetBoxModelSerializer):

    class Meta:
        model = models.CA
        fields = ('pk', 'id', 'name', 'amce', 'tags', 'custom_fields', 'created', 'last_updated')
        
class HostnameSerializer(NetBoxModelSerializer):

    class Meta:
         model = models.Hostname
         fields = ('pk', 'id', 'name', 'ipaddress', 'tags', 'custom_fields', 'created', 'last_updated')