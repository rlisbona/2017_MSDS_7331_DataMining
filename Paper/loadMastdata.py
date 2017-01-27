# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:42:32 2017

@author: joest
"""
import pandas as pd
import os
from pymongo import MongoClient

parent = os.path.dirname(__file__)
refDir = os.path.join(parent, 'Reference Files')
dataDir = os.path.join(parent, 'Census Files')

filename = os.path.join(refDir, 'Mastdata.xls')
Mastdata = pd.read_excel(filename)
print(Mastdata.columns)


client = MongoClient()
try:
    client = MongoClient('localhost', 27017)
    db = client['Census']
    collection = db['Mastdata']

    if collection.count() < 6659:
        for index, row in Mastdata.iterrows():
            if not collection.find({"Item_Id": row["Item_Id"]}).count() > 0:
                collection.insert_one(
                    {
                    "Subject": row["Item_Id"][:3],           
                    "Item_Id": row["Item_Id"],
                    "Item_Description": row["Item_Description"],
                    "Unit_Indicator": row["Unit_Indicator"],
                    "Decimal_Indicator": row["Decimal_Indicator"],
                    "US_Total": row["US_Total"],
                    "Source1": row["Source1"],
                    "Source11": row["Source11"]
                    })
    else:
        print("**Database already exists and is loaded.")
    client.close()
except:
    print("WARNING: unable to connect to Mongo.  Check installation or client info.")
