# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:28:13 2019

@author: ctorr
"""

import pandas

NameList = ["time"]
Dummy = 0
#Open Log File
LogFile = pandas.read_csv("File03.log")

#Grab all 'names'
for index in LogFile.index:
    NameIndex = -1
    if index == 0:
        NameList.append(LogFile.loc[index,"name"])
    else:
        #Step Through NameList to see if name is already used
        for x in NameList:
            NameIndex = NameIndex +1
            if NameList[NameIndex] == LogFile.loc[index,"name"]:
                break
            elif NameIndex == len(NameList)-1:
                NameList.append(LogFile.loc[index,"name"])

#Pull Times into single list and remove duplicates
TimeList = list(dict.fromkeys(LogFile['time'].tolist()))

#Build DF with Column titles
NewFrame = pandas.DataFrame(columns = NameList)
NewFrame.time = TimeList
NewFrame = NewFrame.set_index('time', drop=False)

print(NewFrame)

#Pull All data with same timestamp into one row
#LastTime = ""
for index in LogFile.index:
    for column in NewFrame:
        if column == LogFile.loc[index, "name"]:
            NewFrame.loc[LogFile.loc[index,'time'], LogFile.loc[index,'name']] = LogFile.loc[index, 'value']
           
NewFrame.to_csv('NewFile.csv')              
print(NameList)
print(Dummy)