from netbox.plugins import PluginConfig


class NetBoxCertificatesConfig(PluginConfig):
    name = 'netbox_certificate'
    verbose_name = 'Netbox Certificate Manager'
    description = 'SSL Certificate Manager'
    version = '0.0.1'
    author = 'Eric Hester'
    min_version = '4.0.0'
    author_email = 'hester1@clemson.edu'
    base_url = 'netbox_certificate'


config = NetBoxCertificatesConfig
