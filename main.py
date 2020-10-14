from dearpygui.core import *
from dearpygui.simple import *
from mainwindow import nav, theme, startup, errorcheck
from mainwindow import window as widgets
import base
from packages.richpresence import discord
from packages.chat import gui as chat





if __name__ == '__main__':
    theme.main()
    chat.chat_widget()
    widgets.listed_server()
    discord.RPCThread.start()
    theme.check_theme_on_startup()
    nav.Navigation()
    set_exit_callback(base.FullCloseForDPG)
    start_dearpygui()