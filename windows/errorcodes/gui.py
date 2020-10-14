from dearpygui.simple import *
from dearpygui.core import *
from assets import properties
from windows.errorcodes import functions
import json
import base

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)

def position(sender, data):
    base.center_pos('ErrorcodesWindow')

def window():
    hide_item('MainWindow', children_only=True)

    for widget in properties.MainWindowWidgets:
        hide_item(widget)

    add_window('ErrorcodesWindow',
               label=lang["buttons"]["nav"]["errorcodes"],
               width=1000, height=300, no_resize=True,
               on_close=functions.close)

    add_table('ErrorcodesTable', headers=[lang["buttons"]["nav"]["errorcodes"], lang["errorcodes"]["description"]])

    for langcode in properties.LanguageErrorCodes:
        add_row("ErrorcodesTable", [langcode, lang["errorcodes"]["languages"][langcode], 53])

    for themecode in properties.ThemeErrorCodes:
        add_row("ErrorcodesTable", [themecode, lang["errorcodes"]["themes"][themecode], 53])

    for chatcode in properties.ChatErrorCodes:
        add_row("ErrorcodesTable", [chatcode, lang["errorcodes"]["chat"][chatcode], 53])

    set_render_callback(position)
    end()


def StartWindow(sender, data):
    window()