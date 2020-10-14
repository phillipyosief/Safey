import threading
import time
from pypresence import Presence
from assets import properties

clientid = properties.DiscordRPCClientID
richpresence = Presence(clientid)
richpresence.connect()


def RunRichPresence(stop):
    while True:
        richpresence.update(state=properties.DiscordRPCState,
                            details=properties.DiscordRPCDetails,
                            small_image=properties.DiscordRPCSmallImage,
                            large_image=properties.DiscordRPCLargeImage,
                            small_text=properties.DiscordRPCSmallText,
                            large_text=properties.DiscordRPCLargeText,
                            start=int(time.time()),
                            )
        if stop():
            break



stop_threads = False
RPCThread = threading.Thread(target=RunRichPresence, args=(lambda : stop_threads, ))

