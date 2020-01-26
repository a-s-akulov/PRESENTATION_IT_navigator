import time
import sys
import os
import pyodbc
import win32api
import win32net
import tkinter as tk
from tkinter import messagebox

# PATH DIRS
sys.path.append("functions")
sys.path.append("functions/mode_main")
sys.path.append("gui")
sys.path.append("gui/mode_main")
sys.path.append("gui/kat_gui")

# MY MODULES
import mainWindow
import shopslist_fncs
import other_gui_fncs
import other_fncs
import mode_main_gui
import mode_main_fncs
import kat_switchFrame
import kat_table






class itNavigator():
    def __init__(self):
        #self.MODULES = sys.modules
        self.USERNAME = win32api.GetUserName()
        self.DOMAIN = win32api.GetDomainName()
        self.characterset = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю0123456789"

        self.SELECTED_SHOP = 0
        self.MODE = 0
        self.SHOPS = []
        self.HOSTS = []
        self.HOSTTYPES = []
        self.MASKTYPES = []
        self.FINDER_HANDLE = ["", time.time()]










    def START(self):
        root = mainWindow.firstDraw(self)
        self.root = root
        root.title("IT Navigator - akulov.a")

        
        self.root.mainloop()


main = itNavigator()
main.START()