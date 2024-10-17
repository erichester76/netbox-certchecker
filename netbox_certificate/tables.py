import django_tables2 as tables
from django.utils.translation import gettext as _
from django.utils.html import format_html
from netbox.tables import NetBoxTable, ChoiceFieldColumn, columns
from . import models

class CertificateTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    hostname = columns.ManyToManyColumn(
        verbose_name=_('Hostname'),
        linkify_item=(models.Hostname, {'pk': tables.A('pk')})
    )

    class Meta(NetBoxTable.Meta):
        model = models.Certificate
        fields = ('pk', 'id', 'name', 'cert', 'url', 'alert','comments', 'device', 'actions', )
        default_columns = ('name', 'url' 'cert', 'alert')

class CATable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = models.CA
        fields = ('pk', 'id', 'name', 'acme', 'actions')
        default_columns = ('name', 'acme')

class HostnameTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    ip_address = columns.ManyToManyColumn(
        verbose_name=_('Ip Address'),
        linkify_item=('ipam.ipaddress', {'pk': tables.A('pk')})
    )

    class Meta(NetBoxTable.Meta):
        model = models.Hostname
        fields = ('pk', 'id', 'name', 'ipaddress', 'actions', )
        default_columns = ('name', 'ipaddress')


