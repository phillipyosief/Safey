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

def ignore(sender, data):
    delete_item('Settings' + popups.UnsavedChangesPopupName)
    base.show_main()

def save(sender, data):
    with open('temp/settings.hqs', 'r') as back:
        backup = json.load(back)

    with open('user/settings.hqs', 'w') as user:
        user.write('{\n'
                   f'    "username": "{backup["username"]}",\n'
                   f'    "theme": "{backup["theme"]}",\n'
                   f'    "language": "{backup["language"]}"\n'
                   '}')
        user.close()
        if does_item_exist('SettingsWindow'):
            hide_item('SettingsWindow')
            delete_item('SettingsWindow')
        elif does_item_exist('Settings' + popups.UnsavedChangesPopupName):
            delete_item('Settings' + popups.UnsavedChangesPopupName)
        else:
            pass
        base.show_main()

def close(sender, data):
    with open('temp/settings.hqs', 'w') as user:
        user.write('{\n'
                   f'    "username": "{get_value("Username")}",\n'
                   f'    "theme": "{get_value("Themes")}",\n'
                   f'    "language": "{get_value("Language")}"\n'
                   '}')
        user.close()
    delete_item('SettingsWindow')
    popups.unsaved_changes(save_callback=save, ignore_callback=ignore, name='Settings')


def SessionTheme(sender, data):
    themename = get_value('Themes')
    if themename == 'Dark':
        theme.DefaultTheme()
    else:
        set_theme(themename)
        theme.style()

