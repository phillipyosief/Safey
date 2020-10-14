from dearpygui.core import *
import base

def close(sender, data):
    delete_item('TutorialWindow')
    base.show_main()