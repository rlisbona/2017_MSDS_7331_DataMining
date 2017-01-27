# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 01:17:52 2017

@author: Joe Stoffa & Chris Farrar, Mike Martos, and Randy Lisbona

Master DevNote - Code is suitable for Data Mining project, subsequent DevNotes
are for further code development and public release of the combined county
Census data dataset.
"""

import pandas as pd
import os
import urllib
import requests
import json
from zipfile import ZipFile
from lxml import html

#DevNote switch out code to read parent directory from directory script is
#called.
#DevNote move these values to makefile
parent = os.path.dirname(__file__)  
refDir = os.path.join(parent, 'Reference Files')
dataDir = os.path.join(parent, 'Census Files')
#----End move vars to make file

downloadURL = 'https://www.census.gov/support/USACdataDownloads.html'
refBaseURL = 'http://www2.census.gov/prod2/statcomp/usac/excel/'
refZipURL = 'http://www2.census.gov/prod2/statcomp/usac/zip/'

#make directories for storing reference and data files if they don't 
#already exist
for dir in [refDir, dataDir]:
    try:
        os.stat(dir)
    except:
        os.mkdir(dir)
        print("Created ",dir)


#get lists of reference and data files from Census.gov
page = requests.get(downloadURL)
tree = html.fromstring(page.content)
refFileNames = tree.xpath('//*[@summary="data files for download"]/tr[2]//a/text()')
refFileNames.remove("Ref.zip")    
ZipFileNames = tree.xpath('//*[@summary="data files for download"]//td[3]//a/text()')
ZipFileNames.remove("Ref.zip")


#tired of writing os.path.isfile...
def checkFile(filename):
    return(os.path.isfile(filename))

#download reference files if missing (where accidently deleted or moved)
for file in refFileNames:
    fullpath = os.path.join(refDir, file)    
    if not checkFile(fullpath):
        print("Downloading ", file)        
        urllib.request.urlretrieve(refBaseURL+file, fullpath)

#download Zipped data files if no download record
##specify file to store downloaded file names and their parent zip folder
jsonFile = 'downloadedFiles.json'
jsonFileFullpath = os.path.join(parent, jsonFile)

##if no checkfile is present download all the zipped datafiles
##DevNote - add in error catching/reporting example: failed to download zip
if not checkFile(jsonFileFullpath):
    downloadedFiles = {}    
    for file in ZipFileNames:
        fullpath = os.path.join(dataDir, file)    
        print("Downloading ", file)        
        urllib.request.urlretrieve(refZipURL+file, fullpath)
        zf = ZipFile(fullpath)
        
        ###catch names of downloaded files and their parent zip archive   
        for name in zf.namelist():
            downloadedFiles[name] = file
        print("Extracting ", file)
        zf.extractall(dataDir)
        zf.close()
        os.remove(fullpath)
        
        ###write names of download files and their parent zip folders to file         
        with open(jsonFileFullpath, "w") as fout:
            json.dump(downloadedFiles, fout)

##if file exists open and read it - will use it to find any missing files
else:
    with open(jsonFileFullpath) as json_data:
        downloadedFiles = json.load(json_data)

#check to see if any files are missing (where accidently deleted or moved)
#by referencing json log
zipList = []
dirList = os.listdir(dataDir)
#dirList.remove(jsonFile)
for file in downloadedFiles.keys():
    if file not in dirList:
        zipList.append(downloadedFiles[file])

#download and extract missing zips
#DevNote - need to write code to respond to missing zip files (could not be
#initially downloaded)
for file in zipList:
    fullpath = os.path.join(dataDir, file)    
    print("Downloading ", file)        
    urllib.request.urlretrieve(refZipURL+file, fullpath)
    zf = ZipFile(fullpath)
    print("Extracting ", file)
    zf.extractall(dataDir)
    zf.close()
    os.remove(fullpath)

print("**Download and extraction complete.")
print("If their where no other messages, files already present.")