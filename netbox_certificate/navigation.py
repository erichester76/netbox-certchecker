from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu


certificate_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certificate:certificate_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]

cert_items = (
    PluginMenuItem(
        link='plugins:netbox_certificate:certificate_list',
        link_text='Certificates',
        buttons=certificate_buttons
    ),
)

menu = PluginMenu(
    label="Certificates",
    groups=(("CERTIFICATES", cert_items),),
    icon_class="mdi mdi-lan",
)
