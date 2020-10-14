import tkinter as tk
from tkinter import messagebox
import platform
import time
import os
from assets import properties
import json
import base

def FATAL_APP_ERROR(code):
    root = tk.Tk().withdraw()
    try:
        messagebox.showinfo(title=f'{properties.ProductName}: FATAL ERROR',
                        message=f'Get help on {properties.Website}safey/errors.html\n'
                                f'ERROR: {code}')
    except:
        if platform.system() == 'windows':
            with open(f'FATALERROR_{code}_{time.clock()}.vbs', 'w') as bat:
                bat.write(f'x=msgbox("Get help on {properties.Website}safey/errors.html" & vbcr & "ERROR: {code}" ,16, "{properties.ProductName}: FATAL ERROR")')
                bat.close()
                os.system(f'start {os.getcwd()}/FATALERROR_{code}_{time.clock()}.vbs')

        elif platform.system() == 'linux':
            pass
        elif platform.system() == 'darwin':
            pass



