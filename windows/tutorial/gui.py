from dearpygui.simple import *
from dearpygui.core import *
from assets import properties
from windows.tutorial import functions
import json
import base

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)

def position(sender, data):
    base.center_pos('TutorialWindow')

def window():
    hide_item('MainWindow', children_only=True)

    for widget in properties.MainWindowWidgets:
        hide_item(widget)

    add_window('TutorialWindow',
               label=lang["buttons"]["nav"]["tutorial"],
               autosize=True,
               on_close=functions.close)

    if user["language"] == 'english':
        add_image('TutorialTitleImage',
                  value=properties.TitleEnglishLightTutorial,
                  source=properties.TitleEnglishLightTutorial,
                  width=335, height=80)

    elif user["language"] == 'german':
        add_image('TutorialTitleImage',
                  value=properties.TitleGermanLightTutorial,
                  source=properties.TitleGermanLightTutorial,
                  width=335, height=80)

    else:
        add_image('TutorialTitleImage',
                  value=properties.TitleEnglishLightTutorial,
                  source=properties.TitleEnglishLightTutorial,
                  width=335, height=80)

    add_separator()

    add_text('TutorialWindowDescription', default_value=lang["windows"]["tutorial"]["description"])

    set_render_callback(position)
    end()

def StartWindow(sender, data):
    window()