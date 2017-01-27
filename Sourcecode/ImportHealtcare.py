# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:21:01 2017

@author: Randy
"""


# data source = https://data.healthcare.gov/download/f6am-7dvb/application%2Fzip
#%%
import os
cwd = os.getcwd()
print("Current working directory=",cwd,sep='')  

# In Spyder      Current working directory=C:\users\Randy    
# Should be      Current working directory=C:\Users\Randy\Documents\GitHub\2017_MSDS_7331_DataMining\Sourcecode  (where I have a file named ImportHealthcare.py
# in Jupyter     Current working directory=C:\Users\Randy\Documents\GitHub\2017_MSDS_7331_DataMining\Paper

# I need to create a temporary subdirectory from whereever it is running to download and unzip a file.  I would prefer syntax that works in Spyder or Jupyter
# There is a module pathlib that is newer than os, but I can't figure out how to use it.
# https://docs.python.org/3/library/pathlib.html
# I could use help understanding how to read and interpret the python documentation

#%%
#Second question is how to get attribute names and values for a object (I may be using the wrong terminology here)
#For instance the Path() function is supposed to create a path object.
#Is there a generic way to get the attribute names and values for an object. 
#vars() gives me attribute names but not the values
#in the case of the directory path, if I could see all the values, I could figure out which attribute I am looking for
# beeprint seems to do this, but I can't make it work in my code, I don't understand how to call it.
#https://pypi.python.org/pypi/beeprint/2.3.3

#%%
from pathlib import Path
p= Path.cwd()   #gives me C:/Users/Randy when run in Spyder
help(Path)

p.parts
p.parent
dir(os)
help(os)
p.curdir
#%%

os.get_exec_path()
#%%

HealthCareURL = 'https://data.healthcare.gov/download/f6am-7dvb/application%2Fzip'
localfilename = cwd + "\\temp.zip"
print(localfilename)  #C:\users\Randy\temp.zip      I can download the file here but it is not where I want to put it

# This should give me the path but I get a nameerror: name '__file__' is not defined
#print(pathlib.Path(__file__).resolve().parent)

#%%
import requests
req = requests.get(HealthCareURL)
file = open(localfilename,'wb')  #open local temp.zip file to write, wb seems like it must mean write block but not sure

# code example http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls.  SEE section Raw Response Content
# not clear why I need to write the file in chunks, seems like there must be a way to write it in one pass

for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()

# I can't figure out how to get the filename from this URL.  it creates a zip file and the file I want is in it but it seems 
# like I should be able to get a filename for the .zip file from the url and that is stumping me.  It is working if I assign a filename but I would just like to use default name.
# https://data.healthcare.gov/download/wy5p-7apr/application%2Fzip

#%%
from pprint import pprint
#pprint(vars(cwd))


def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %s" % (attr, getattr(obj, attr)))
    
dump(chr)
help(os)