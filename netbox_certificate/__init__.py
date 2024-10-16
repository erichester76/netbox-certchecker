from netbox.plugins import PluginConfig


class NetBoxCertificatesConfig(PluginConfig):
    name = 'netbox_certificate'
    verbose_name = 'Netbox Certificate Manager'
    description = 'SSL Certificate Manager'
    version = '1.0'
    base_url = 'certificates'
    min_version = '3.7.0'


config = NetBoxCertificatesConfig
