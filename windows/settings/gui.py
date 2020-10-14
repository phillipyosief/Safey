from dearpygui.simple import *
from dearpygui.core import *
from assets import properties
from windows.settings import functions
import json
import base
import platform

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)

def position(sender, data):
    base.center_pos('SettingsWindow')

def window():
    hide_item('MainWindow', children_only=True)

    for widget in properties.MainWindowWidgets:
        hide_item(widget)

    add_window('SettingsWindow',
               label=lang["buttons"]["nav"]["settings"],
               autosize=True,
               on_close=functions.close)

    if user["language"] == 'english':
        add_image('SettingsTitleImage',
                  value=properties.TitleEnglishLightSettings,
                  source=properties.TitleEnglishLightSettings,
                  width=335, height=80)

    elif user["language"] == 'german':
        add_image('SettingsTitleImage',
                  value=properties.TitleGermanLightSettings,
                  source=properties.TitleGermanLightSettings,
                  width=335, height=80)

    else:
        add_image('SettingsTitleImage',
                  value=properties.TitleEnglishLightSettings,
                  source=properties.TitleEnglishLightSettings,
                  width=335, height=80)

    add_separator()
    add_combo('Language', default_value=user["language"], items=properties.Languages)

    add_separator()
    add_text('Chat')
    add_input_text('Username', hint=user["username"])
    add_text('Design')
    add_combo('Themes', default_value=user["theme"], items=properties.Themes, callback=functions.SessionTheme)

    add_separator()

    add_text('SettingsVersionText',
             default_value=f'Safey {properties.ProductVersion}\n'
             f'Dear PyGui {get_dearpygui_version()}\n'
             f'Python {platform.python_version()}\n'
             f'{platform.platform()}')
    set_item_color("SettingsVersionText", mvGuiCol_Text, (113, 113, 113))

    add_separator()
    add_button(name='SettingsCloseButton', label=lang["buttons"]["windows"]["settings"]["close"],
               callback=functions.close)
    add_same_line()
    add_button(name='SettingsSaveButton', label=lang["buttons"]["windows"]["settings"]["save"],
               callback=functions.save)




    set_render_callback(position)
    end()

def StartWindow(sender, data):
    window()