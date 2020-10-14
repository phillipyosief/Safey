from dearpygui.simple import *
from dearpygui.core import *
from assets import properties
from windows.discord import functions
import json
import base
import platform
from mainwindow import webfunc

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)

def position(sender, data):
    base.center_pos('DiscordWindow')

def close(sender, data):
    base.show_main()
    delete_item('DiscordWindow', children_only=True)
    delete_item('DiscordWindow')

def window():
    hide_item('MainWindow', children_only=True)

    for widget in properties.MainWindowWidgets:
        hide_item(widget)

    add_window('DiscordWindow',
               label=lang["buttons"]["nav"]["discord"],
               autosize=True, on_close=close)
    add_image('DiscordTitleImage',
              value=properties.DiscordLogo,
              source=properties.DiscordLogo,
              width=100, height=100)
    add_same_line()
    with group('DiscordDescriptionGroup'):
        add_text('Discord')
        add_separator()
        add_text(lang["windows"]["discord"]["description"])

        add_button(name='DiscordJoinhqsartworksButton', label=lang["buttons"]["windows"]["discord"]["join_hqsartworks"],
                   callback=webfunc.hqsartworksServerInvite)
        add_same_line()
        add_button(name='DiscordJoinAlphaclanButton', label=lang["buttons"]["windows"]["discord"]["join_alphaclan"],
                   callback=webfunc.AlphaclanServerInvite)

    set_render_callback(position)
    end()

def StartWindow(sender, data):
    window()