import webbrowser
from assets import properties
import subprocess

def hqsartworks(sender, data):
    webbrowser.open_new_tab(url=properties.Website)

def hqsbotInvite(sender, data):
    webbrowser.open_new_tab(url=f'{properties.Website}/invitelink.html')

def hqsartworksServerInvite(sender, data):
    webbrowser.open_new_tab(url=f'{properties.hqsartworksDiscordInvite}')

def AlphaclanServerInvite(sender, data):
    webbrowser.open_new_tab(url=f'{properties.AlphaclanDiscordInvite}')

def DevInstagram(sender, data):
    webbrowser.open_new_tab(url=f'https://www.instagram.com/{properties.DevInstagram}')

def OrgInstagram(sender, data):
    webbrowser.open_new_tab(url=f'https://www.instagram.com/{properties.OrgInstagram}')

def DevTwitter(sender, data):
    webbrowser.open_new_tab(url=f'https://www.twitter.com/{properties.DevTwitter}')

def OrgTwitter(sender, data):
    webbrowser.open_new_tab(url=f'https://www.twitter.com/{properties.OrgTwitter}')

def DevSnapchat(sender, data):
    webbrowser.open_new_tab(url=f'https://www.snapchat.com/add/{properties.DevSnapchat}')

def OrgSnapchat(sender, data):
    webbrowser.open_new_tab(url=f'https://www.snapchat.com/{properties.OrgSnapchat}')

def mailto_contact(sender, data):
    subprocess.Popen(['start', 'mailto:contact@hqsartworks.me'])

def alphaclanWebsite(sender, data):
    webbrowser.open_new_tab(url=f'{properties.AlphaclanServerIP}')

def jailbreakInviteLink(sender, data):
    webbrowser.open_new_tab(url=f'{properties.JailbreakInviteLink}')