from dearpygui.core import *
from dearpygui.simple import *
import base
from mainwindow import theme
from presets import popups
import json
from assets import properties

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)


def close(sender, data):
    delete_item('QandAWindow')
    base.show_main()



