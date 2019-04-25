# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as GUI

def SelectFile():
    print("Log File Path")
    
def SelectFolder():
    print("Export File Path")
    
#Create Main Window    
MainWindow = GUI.Tk()

#Define Frames in Main Window
FileFrame = GUI.Frame(master=MainWindow, width=600, height=200, bd=1, relief="sunken")
OutputFrame = GUI.Frame(master=MainWindow, width=300, height=260, bd=1, relief="sunken")
OptionFrame = GUI.Frame(master=MainWindow, width=300, height=260, bd=1, relief="sunken")

#Define Widgets in FileFrame
LoadFileLabel = GUI.Label(master=FileFrame, text="Log File Path:")
ExportLocationLabel = GUI.Label(master=FileFrame, text="Export File Path:")

#Pack FileFrame Widgets
LoadFileLabel.pack()
ExportLocationLabel.pack()

#Pack Frames
FileFrame.pack()
OutputFrame.pack(side="left")
OptionFrame.pack(side="right")

MainWindow.mainloop()
