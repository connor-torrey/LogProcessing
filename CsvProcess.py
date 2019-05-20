# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:05:19 2019

@author: C. Torrey
Desc: CsvProcess opens a selected file and divides it into columns
TODO: - Add interpolation, linear/quadratic/cubic
      - Add Plotting option, stacked, single charts
      - Restructure for easier maintenance/usage
      - Deal with incomplete last entry issue
"""

#import csv as FileReader
#
#with open('File01.log') as csv_file:
#    CsvReader = FileReader.reader(csv_file, delimiter=',')
#    LineCount = 0
#    
#    for row in CsvReader: 
#        if LineCount == 0:

import pandas

#Open .log File and read into LogFile dataframe
LogFile = pandas.read_csv('File01.log')

#Create an empty dataframe to put selected data with same column names as LogFile
NewFile = pandas.DataFrame(columns=LogFile.columns)

#Print Check
print(LogFile)

#Step through LogFile and pull out all rows with desired name
NewIndex = 0
for index in LogFile.index:
    if LogFile.loc[index, 'name'] == 'EngineRPM':
        NewFile.loc[NewIndex, :] = LogFile.loc[index,:]
        print(LogFile.loc[index, 'name'])

#print Check
print(NewFile)

#Remove enum column from new DataFrame
NewFile = NewFile.drop(columns="enum", axis=1)

#Print Check
print(NewFile)

#Export NewFile to CSV
NewFile.to_csv('NewFile.csv', index=False)