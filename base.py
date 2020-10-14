from dearpygui.core import *
from dearpygui.simple import *
from packages.richpresence import discord
from assets import properties
import main

def recursively_show(container):
    for item in get_item_children(container):
        if get_item_children(item):
            show_item(item)
            recursively_show(item)
        else:
            show_item(item)

def center_pos(item):
    if does_item_exist(item):
        main_width = get_item_width('MainWindow')
        main_height = get_item_height('MainWindow')
        item_width = get_item_width(item)
        item_height = get_item_height(item)
        set_window_pos(item, int((main_width/2 - item_width/2)), int((main_height/2 - item_height/2)))
    else:
        set_render_callback(None)


def show_main():
    for widget in properties.MainWindowWidgets:
        show_item(widget)
    recursively_show('MainWindow')


def FullCloseForDPG(sender, data):
    discord.stop_threads = True
    discord.RPCThread.join()
    exit()


def FullClose():
    discord.stop_threads = True
    discord.RPCThread.join()
    exit()
