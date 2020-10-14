from dearpygui.simple import *
from dearpygui.core import *
import requests
import socket
import json

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = user["username"].encode('ascii')

def check_if_server_online(sender, data):
    hide_item('ListedServerStatus?Text')
    hide_item('ListedServerStatusONLINEText')
    hide_item('ListedServerStatusOFFLINEText')
    try:
        requests.get('http://' + get_value('IP') + ':' + str(get_value('Port')))

        show_item('ListedServerStatusONLINEText')
        set_item_color('ListedServerStatusONLINEText', mvGuiCol_Text, (9, 184, 0, 255))
    except Exception as e:
        show_item('ListedServerStatusOFFLINEText')
        set_item_color('ListedServerStatusOFFLINEText', mvGuiCol_Text, (184, 18, 0, 255))
        print(e)
