import json
import socket
import threading
from dearpygui.core import *
from dearpygui.simple import *

with open('user/settings.hqs', 'r') as usersettings:
    user = json.load(usersettings)

with open(f'languages/{user["language"]}.hqs', 'r') as language:
    lang = json.load(language)


username = 'test'
FORMAT = 'utf-8'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def show(msg):
    delete_item('ChatWidget')
    add_window('ChatWidget', no_title_bar=True, no_move=True,
               width=875, height=600, x_pos=400, y_pos=15,
               no_resize=False)
    add_text(get_value('IP'))
    add_separator()
    add_text(msg)

def connect(sender, data):
    client.connect((get_value('IP'), get_value('Port')))
    #rcv = threading.Thread(target=receive)
    #rcv.start()
    run_async_function(receive, 'RECEIVE FUNCTION')

def sendButton(sender, data):
    receive(sender='', data='')



# function to receive messages
def receive(sender, data):
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)

            # if the messages from the server is NAME send the client's name
            if message == 'NAME':
                client.send(username.encode(FORMAT))
            else:
                add_text(message)
        except:
            # an error will be printed on the command line or console if there's an error
            print("An error occured!")
            client.close()
            break

        # function to send messages


def sendMessage(self):
    while True:
        message = (f"{self.name}: {self.msg}")
        client.send(message.encode(FORMAT))
        break

