# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:33:17 2022

@author: wetlab
"""

import zipfile
import tkinter as tk
import os
from tkinter import filedialog
#%%
currWD = os.getcwd()
print(currWD)
currWDFiles = os.listdir(currWD)
print('Files in the directory:',currWDFiles)
# Ask user if is the correct one. If not, select the right one.
root = tk.Tk()
root.withdraw()
title = 'Current Working Directory'
message = 'Is this the correct working directory'
workDir = tk.messagebox.askquestion(title, message)
if workDir == 'yes':
    yesTitle = 'YES!'
    yesMessage = 'Go ahead to the next section of the code'
    tk.messagebox.showinfo(yesTitle, yesMessage)
else:
    noTitle = 'NO!'
    noMessage = 'Ok! Select the correct one'
    tk.messagebox.showinfo(noTitle, noMessage)
    newWorkDir = filedialog.askdirectory()
    newDir = os.chdir(newWorkDir)
    print(newDir)
    newDirFiles = os.listdir(newDir)
    print('Files in the directory:', newDirFiles)
#%%
currWD = os.getcwd()
fileList = os.listdir(currWD)
print(len(fileList))
#%%
# 488 canal
# Choose the directory where to extract the files
targetDir = filedialog.askdirectory()
for file in fileList:
    if file.startswith('488'):
        fileZip = zipfile.ZipFile(file, 'r', 
                                  allowZip64=True)
        fileZip.extractall(targetDir)
#%%
# 561 canal
# Choose the directory where to extract the files
targetDir = filedialog.askdirectory()
for file in fileList:
    if file.startswith('561'):
        fileZip = zipfile.ZipFile(file, 'r', 
                                  allowZip64=True)
        fileZip.extractall(targetDir)
#%%
# 647 canal
# Choose the directory where to extract the files
targetDir = filedialog.askdirectory()
for file in fileList:
    if file.startswith('647'):
        fileZip = zipfile.ZipFile(file, 'r', 
                                  allowZip64=True)
        fileZip.extractall(targetDir)

print("Unzipping process is over!")