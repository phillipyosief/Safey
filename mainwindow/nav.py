from dearpygui.simple import *
from dearpygui.core import *
from assets import properties
from mainwindow import webfunc
from windows.about import gui as about
from windows.discord import gui as discord
from windows.settings import gui as settings
from windows.qanda import gui as qanda
from windows.errorcodes import gui as errorcodes
from windows.tutorial import gui as tutorial
import json

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)



def Image():
    add_image_button(name='NavigationImageButton',
                     value=properties.SafeyLogoLight,
                     tip=f'{properties.ProductName}, {properties.ProductVersion}',
                     width=100, height=100,
                     callback=webfunc.hqsartworks)

    set_item_color("NavigationImageButton", mvGuiCol_Button, (0, 0, 0, 0))
    set_item_color("NavigationImageButton", mvGuiCol_ButtonHovered, (0, 0, 0, 0))
    set_item_color("NavigationImageButton", mvGuiCol_ButtonActive, (0, 0, 0, 0))

def Buttons():
    with group('NavigationButtonsGroup'):
        add_button('NavigationSettingsButton', label=lang["buttons"]["nav"]["settings"], width=90, height=25,
                   callback=settings.StartWindow)
        add_button('NavigationTutorialButton', label=lang["buttons"]["nav"]["tutorial"], width=90, height=25,
                   callback=tutorial.StartWindow)
        add_button('NavigationQandAButton', label=lang["buttons"]["nav"]["q&a"], width=90, height=25,
                   callback=qanda.StartWindow)
        add_button('NavigationDiscordButton', label=lang["buttons"]["nav"]["discord"], width=90, height=25,
                   callback=discord.StartWindow)
        add_button('NavigationAboutButton', label=lang["buttons"]["nav"]["about"], width=90, height=25,
                   callback=about.StartWindow)
        add_button('NavigationErrorButton', label=lang["buttons"]["nav"]["errorcodes"], width=90, height=25,
                   callback=errorcodes.StartWindow)



def Navigation():
    Image()
    Buttons()


