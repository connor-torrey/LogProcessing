# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:54:16 2019

@author: ctorr
"""
class GUI:
    FileName = "C:\something"
    
    def start():
        print("Started")
        
    def stop():
        print("Stopped")
    
    #Opens File Explorer, returns file path
    def SelectFile():
        from tkinter import filedialog
        
        FileString = filedialog.askopenfilename()
        return FileString
        
    
    def Main_Dialog():
        #Declare GUI as a tkinter object
        import tkinter
        #Don't necessarily have to rename objects
        """import tkinter"""

        #Opens Dialog
        root = tkinter.Tk()
        
        #GUI Box Title/Icon Image
        root.title("Log File Processing")
        root.iconbitmap(r'Images\H_Logo.ico')
        root.geometry('600x500')
        
        #Choose File 
        #Create Text Output
        fileOutputBox = tkinter.Message(root, width=300,
                                        text=GUI.FileName)
        fileOutputBox.pack(side=tkinter.LEFT, anchor=tkinter.N)

        #Creates a label widget in center of dialog
        w = tkinter.Label(root, text="Hello Tkinter")
        w.pack()

        #Create Side By side Buttons
        button = tkinter.Button(root, text="QUIT",
                            fg="red",
                            command=GUI.stop)
        button.pack(side=tkinter.LEFT)

        button2 = tkinter.Button(root, text="Start",
                             fg="green",
                             command=GUI.start)
        button2.pack(side=tkinter.LEFT)

        #Basically a function call
        root.mainloop()
    
    def OpenFile():
        print("openFile")
    
defaultGUI = GUI

defaultGUI.Main_Dialog()