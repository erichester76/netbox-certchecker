from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from . import serializers

class CertificateViewSet(NetBoxModelViewSet):
    queryset = models.Certificate.objects.prefetch_related('tags')
    serializer_class = serializers.CertificateSerializer
    
class CAViewSet(NetBoxModelViewSet):
    queryset = models.Certificate.objects.prefetch_related('tags')
    serializer_class = serializers.CASerializer
    
class HostnameViewSet(NetBoxModelViewSet):
    queryset = models.Hostname.objects.prefetch_related('tags')
    serializer_class = serializers.HostnameSerializer
