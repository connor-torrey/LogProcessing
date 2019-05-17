# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:34:43 2019

@author: ctorr
"""

from tkinter import filedialog
import tkinter

root = tkinter.Tk()
root.filename = filedialog.askopenfilename(initialdir = "/",
                                           title = "Select File")