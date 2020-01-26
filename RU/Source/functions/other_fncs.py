
import tkinter as tk

def fatal_error(self, text):
    import tkinter.messagebox as mb
    import sys

    mb.showerror("Error", text)
    sys.exit(0)