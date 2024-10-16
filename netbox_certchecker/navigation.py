from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

certchecker_buttons = [
    PluginMenuButton(
        link='plugins:netbox_certchecker:certificate_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    )
]



cert_items = (
    PluginMenuItem(
        link='plugins:netbox_certchecker:certificate_list',
        link_text='Certificates',
        buttons=certchecker_buttons
    ),
)

menu = PluginMenu(
    label="Certificates",
    groups=(("CERTIFICATES", cert_items),),
    icon_class="mdi mdi-lan",
)
