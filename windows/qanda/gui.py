from dearpygui.simple import *
from dearpygui.core import *
from assets import properties
from windows.qanda import functions
import json
import base
import platform

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)

def position(sender, data):
    base.center_pos('QandAWindow')

def window():
    hide_item('MainWindow', children_only=True)

    for widget in properties.MainWindowWidgets:
        hide_item(widget)

    add_window('QandAWindow',
               label=lang["buttons"]["nav"]["q&a"],
               autosize=True,
               on_close=functions.close)

    if user["language"] == 'english':
        add_image('QandATitleImage',
                  value=properties.TitleEnglishLightSettings,
                  source=properties.TitleEnglishLightSettings,
                  width=335, height=80)

    elif user["language"] == 'german':
        add_image('QandATitleImage',
                  value=properties.TitleGermanLightQandA,
                  source=properties.TitleGermanLightQandA,
                  width=335, height=80)

    else:
        add_image('QandATitleImage',
                  value=properties.TitleEnglishLightQandA,
                  source=properties.TitleEnglishLightQandA,
                  width=335, height=80)

    add_separator()

    add_text(name='QandAQuestion1', default_value=f'{lang["text"]["q&a"]["1"]["question"]}\n\n'
                                                  f'{lang["text"]["q&a"]["1"]["answer"]}')
    add_separator()
    add_text(name='QandAQuestion2', default_value=f'{lang["text"]["q&a"]["2"]["question"]}\n\n'
                                                  f'{lang["text"]["q&a"]["2"]["answer"]}')

    set_render_callback(position)
    end()

def StartWindow(sender, data):
    window()