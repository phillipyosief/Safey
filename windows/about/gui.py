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
    base.center_pos('AboutWindow')

def close(sender, data):
    base.show_main()
    delete_item('AboutWindow', children_only=True)
    delete_item('AboutWindow')

def window():
    hide_item('MainWindow', children_only=True)

    for widget in properties.MainWindowWidgets:
        hide_item(widget)

    add_window('AboutWindow',
               label=lang["buttons"]["nav"]["about"],
               autosize=True, on_close=close)

    add_image('AboutTitleImage',
              value=properties.SafeyLogoLight,
              source=properties.SafeyLogoLight,
              width=110, height=110)
    add_same_line()
    with group('AboutDescriptionGroup'):
        add_text('AboutDescription', default_value=lang["windows"]["about"]["description"])

        add_separator()

        add_button(name='AboutGitHubRepoButton', label=lang["buttons"]["windows"]["about"]["github_repo"],
                   callback=webfunc.AlphaclanServerInvite)
        add_same_line()
        add_button(name='AboutWebsiteButton', label=lang["buttons"]["windows"]["about"]["website"],
                   callback=webfunc.AlphaclanServerInvite)
        add_same_line()
        add_button(name='AboutDiscordButton', label=lang["buttons"]["windows"]["about"]["discord"],
                   callback=webfunc.AlphaclanServerInvite)
        add_same_line()
        set_render_callback(position)
        end()

def StartWindow(sender, data):
    window()