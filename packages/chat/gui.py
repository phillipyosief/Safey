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


def chat_widget():
    add_window('ChatWidget', no_title_bar=True, no_move=True,
               width=875, height=600, x_pos=400, y_pos=15,
               no_resize=False)
    add_text('ChatWidgetServerName', default_value='Server Name')
    add_separator()
    end()

    add_window('ChatWidgetMessage', no_title_bar=True, no_move=True,
               width=875, height=40, x_pos=400, y_pos=620,
               no_resize=False)

    add_input_text(lang["main"]["chat"]["message"], hint=lang["main"]["chat"]["message"])
    add_same_line()
    add_button(lang["main"]["chat"]["send"], callback=client.sendButton)
    end()

    add_window('ServerDescriptionWidget', no_title_bar=True, no_move=True,
               width=875, height=40, x_pos=400, y_pos=665,
               no_resize=False)

    add_text('ServerInfoText', default_value=lang["main"]["serverinfo"])
    end()