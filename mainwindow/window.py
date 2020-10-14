from dearpygui.core import *
from dearpygui.simple import *
from assets import properties
import json
from mainwindow import webfunc
from packages.chat import client

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)

def new_server(name, image, description, ip, callback_website):
    add_image(f'{name}PublicServerImage',
              value=image, width=60, height=60)
    add_same_line()
    with group(f"{name}PublicServerInfo"):
        add_text(f'{name}\n'
                 f'IP: {ip}', tip=description)
        add_button(f'{name}PublicServerConnectButton', label=lang["main"]["listedserver"]["connect"], width=92)
        add_same_line()
        add_button(f'{name}PublicServerWebsiteButton', label='Website', width=92, callback=callback_website)




def listed_server():
    add_window('ListedServerWindow', no_title_bar=True, no_move=True, no_resize=True,
               autosize=True, x_pos=110, y_pos=15, no_close=True)
    add_text(lang["main"]["listedserver"]["title"])

    add_separator()

    new_server('Safey public', properties.SafeyLogoLight,
               'Official Safey chatroom (Language: English)',
               properties.SafeyServerIP, callback_website=webfunc.hqsartworks)

    add_separator()

    new_server('alphaclan community', properties.AlphaclanLogo,
               'alphaclan community server (Language: German)',
               properties.AlphaclanServerIP, callback_website=webfunc.alphaclanWebsite)

    add_separator()

    new_server('Jailbreak chatroom', properties.JailbreakLogo,
               'All about jailbreaking Apple devices (Language: German)',
               properties.JailbreakServerIP, callback_website=webfunc.jailbreakInviteLink)

    add_separator()

    add_text(lang["main"]["listedserver"]["connect_with_server"])

    add_input_text('IP', hint='example.com')
    add_input_int('Port')

    add_button('ListedServerCustomServerConnectButton', label=lang["main"]["listedserver"]["connect"],
               callback=client.connect)
    add_same_line()
    add_text('ListedServerStatus?Text', default_value='STATUS: ?')

    add_text('ListedServerStatusONLINEText', default_value='STATUS: ONLINE')
    add_text('ListedServerStatusOFFLINEText', default_value='STATUS: OFFLINE')

    hide_item('ListedServerStatusONLINEText')
    hide_item('ListedServerStatusOFFLINEText')

    end()

def chat_window():
    pass