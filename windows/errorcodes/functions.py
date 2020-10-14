from dearpygui.simple import *
from dearpygui.core import *
import base

def close(sender, data):
    delete_item('ErrorcodesWindow')
    base.show_main()