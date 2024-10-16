from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu


cert_items = (
    PluginMenuItem(
        link='plugins:netbox_certificate:ca_list',
        link_text='Certificate Authorities',
        buttons=[
            PluginMenuButton(
            link='plugins:netbox_certificate:ca_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
        )]
    ),
    PluginMenuItem(
        link='plugins:netbox_certificate:certificate_list',
        link_text='Certificates',
        buttons=[
            PluginMenuButton(
            link='plugins:netbox_certificate:certificate_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
        )]
    ),
    PluginMenuItem(
        link='plugins:netbox_certificate:hostname_list',
        link_text='Hostnames',
        buttons=[
            PluginMenuButton(
            link='plugins:netbox_certificate:hostname_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
        )]
    ),
)

menu = PluginMenu(
    label="Certificates",
    groups=(("CERTIFICATES", cert_items),),
    icon_class="mdi mdi-lan",
)
