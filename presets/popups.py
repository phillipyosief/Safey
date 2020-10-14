from dearpygui.simple import *
from dearpygui.core import *
from assets import properties
from packages import security
import base
import json

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)

UnsavedChangesPopupName = 'UnsavedChangesPopup'

def unsaved_changes(save_callback, ignore_callback, name):
    def position(sender, data):
        base.center_pos(f'{name}UnsavedChangesPopup')

    add_window(f'{name}UnsavedChangesPopup',
               width=610, height=142,
               no_title_bar=True, no_resize=True, no_scrollbar=True)

    add_image(f'{name}UnsavedChangesPopupWarningImage', value=properties.WarningIcon, width=100, height=100)
    add_same_line()
    with group(f"{name}UnsavedChangesPopupDescription"):
        add_text(lang["errors"]["warning"])
        add_separator()
        add_text(lang["errors"]["unsaved_changes"]["description"])

    add_button(f'{name}UnsavedChangesPopupWarningSaveButton',
               label=lang["errors"]["unsaved_changes"]["save"], width=300, callback=save_callback)

    add_same_line()

    add_button(f'{name}UnsavedChangesPopupWarningIgnoreButton',
               label=lang["errors"]["unsaved_changes"]["ignore"], width=300, callback=ignore_callback)
    set_item_color(f"{name}UnsavedChangesPopupWarningIgnoreButton", mvGuiCol_ButtonHovered, (192, 30, 28, 255))
    set_item_color(f"{name}UnsavedChangesPopupWarningIgnoreButton", mvGuiCol_ButtonActive, (192, 30, 28, 255))

    set_render_callback(position)
    end()

def security_alert(ignore_callback, name):
    def position(sender, data):
        base.center_pos(f'{name}SecurityAlertPopup')

    add_window(f'{name}SecurityAlertPopup',
               width=610, height=142,
               no_title_bar=True, no_resize=True, no_scrollbar=True)

    add_image(f'{name}SecurityAlertPopupSecurityAlertImage', value=properties.SecurityalertIcon, width=100, height=100)
    add_same_line()
    with group(f"{name}SecurityAlertPopupDescription"):
        add_text(lang["errors"]["error"])
        add_separator()
        add_text(lang["errors"]["security_alert"]["description"])

    add_button(f'{name}SecurityAlertPopupInstallButton',
               label=lang["errors"]["security_alert"]["install"], width=300, callback=security.install)

    add_same_line()

    add_button(f'{name}SecurityAlertPopupIgnoreButton',
               label=lang["errors"]["unsaved_changes"]["ignore"], width=300, callback=ignore_callback)
    set_item_color(f"{name}SecurityAlertPopupIgnoreButton", mvGuiCol_ButtonHovered, (192, 30, 28, 255))
    set_item_color(f"{name}SecurityAlertPopupIgnoreButton", mvGuiCol_ButtonActive, (192, 30, 28, 255))

    set_render_callback(position)
    end()

def fatal_error(name, code, category):
    def position(sender, data):
        base.center_pos(f'{name}FatalErrorPopup')

    add_window(f'{name}FatalErrorPopup',
               width=610, height=142,
               no_title_bar=True, no_resize=True, no_scrollbar=True)

    add_image(f'{name}FatalErrorPopupErrorImage', value=properties.ErrorIcon, width=100, height=100)
    add_same_line()
    with group(f"{name}FatalErrorPopupDescription"):
        add_text(lang["errors"]["error"])
        add_separator()
        add_text(lang["errorcodes"][category][code])

    add_button(f'{name}FatalErrorPopupExitButton',
               label=lang["errors"]["exit"], width=600, callback=base.FullClose)

    set_item_color(f"{name}FatalErrorPopupExitButton", mvGuiCol_ButtonHovered, (192, 30, 28, 255))
    set_item_color(f"{name}FatalErrorPopupExitButton", mvGuiCol_ButtonActive, (192, 30, 28, 255))

    set_render_callback(position)
    end()

