# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:30:32 2017

@author: Randy
"""

#Get path to Data directory with downloaded .csv files
#%%
import os
jupyterDir = os.path.realpath('../')
print('Proj -', jupyterDir)
csvDir = os.path.join(jupyterDir,'Data')
def chk_dir(csvdir):
    if not os.path.exists(csvdir):
        os.makedirs(csvdir)
#%%        
chk_dir(csvDir)
print(csvDir)
os.listdir(csvDir)
#%%
#Import the 2017 Healthcare Individual Market Dental data
#sourced from    https://data.healthcare.gov/dataset/2017-QHP-Landscape-Individual-Market-Dental-Excel/f6am-7dvb

import pandas as pd
infile = '2017_QHP_Landscape_Individual_Market_Dental.csv'
outfile = '2017_QHP_Landscape_Individual_Market_Dental_clean.csv'
infilepath = csvDir + '\\'+ infile
outfilepath = csvDir +'\\'+ outfile
print(infilepath)

print(pd.get_option('max_columns'))

pd.set_option('max_columns',100)
pd.set_option('expand_frame_repr', True)
pd.set_option('large_repr','info')
#define a mapping dictionary for fields as needed
#FIPS County Code - Was stripping leading zeros and coming in as a number, it is a zip code

# clean up the fieldnames to remove spaces, + and commas
dtype_dict = {'FIPS County Code': str,'State Code': str}
df = pd.read_csv(infilepath,header ='infer',sep=',',dtype=dtype_dict) # ,nrows=50 to limit the number of rows
df.columns = [c.replace(' ','_') for c in df.columns]
df.columns = [c.replace(',','') for c in df.columns]
df.columns = [c.replace('_-_','') for c in df.columns]
df.columns = [c.replace('+','_') for c in df.columns]

df.columns
print('state code type',type(df.State_Code))
print(list(df))
df.columns.tolist()
#print(df)
#print(df.dtypes)
#print(df.head(5))
df.describe()
df
#Note the output below shows the first few and last few columns and first few and last few rows
#How to show all columns?

#%%  Set the field types, strip $ and other garbage 
import decimal
D = decimal.Decimal

df["State_Code"]=df["State_Code"].astype(str)
df["FIPS_County_Code"]=df["FIPS_County_Code"].astype(str)
df["County_Name"]=df["County_Name"].astype(str)
df["Metal_Level"]=df["Metal_Level"].astype(str)
df["Issuer_Name"]=df["Issuer_Name"].astype(str)
df["HIOS_Issuer_ID"]=df["HIOS_Issuer_ID"].astype(str)
df["Plan_ID_(Standard_Component)"]=df["Plan_ID_(Standard_Component)"].astype(str)
df["Plan_Marketing_Name"]=df["Plan_Marketing_Name"].astype(str)
df["Plan_Type"]=df["Plan_Type"].astype(str)
df["Rating_Area"]=df["Rating_Area"].astype(str)
df["Child_Only_Offering"]=df["Child_Only_Offering"].astype(str)
df["Source"]=df["Source"].astype(str)
df["Customer_Service_Phone_Number_Local"]=df["Customer_Service_Phone_Number_Local"].astype(str)
df["Customer_Service_Phone_Number_Toll_Free"]=df["Customer_Service_Phone_Number_Toll_Free"].astype(str)
df["Customer_Service_Phone_Number_TTY"]=df["Customer_Service_Phone_Number_TTY"].astype(str)
df["Network_URL"]=df["Network_URL"].astype(str)
df["Plan_Brochure_URL"]=df["Plan_Brochure_URL"].astype(str)
df["Summary_of_Benefits_URL"]=df["Summary_of_Benefits_URL"].astype(str)
df["Drug_Formulary_URL"]=df["Drug_Formulary_URL"].astype(str)
df["Routine_Dental_ServicesAdult_(Coverage)"]=df["Routine_Dental_ServicesAdult_(Coverage)"].astype(str)
df["Basic_Dental_CareAdult_(Coverage)"]=df["Basic_Dental_CareAdult_(Coverage)"].astype(str)
df["Major_Dental_CareAdult_(Coverage)"]=df["Major_Dental_CareAdult_(Coverage)"].astype(str)
df["OrthodontiaAdult_(Coverage)"]=df["OrthodontiaAdult_(Coverage)"].astype(str)
df["Dental_Check-Up_for_Children_(Coverage)"]=df["Dental_Check-Up_for_Children_(Coverage)"].astype(str)
df["Basic_Dental_CareChild_(Coverage)"]=df["Basic_Dental_CareChild_(Coverage)"].astype(str)
df["Major_Dental_CareChild_(Coverage)"]=df["Major_Dental_CareChild_(Coverage)"].astype(str)
df["OrthodontiaChild_(Coverage)"]=df["OrthodontiaChild_(Coverage)"].astype(str)
df["Premium_Rates"]=df["Premium_Rates"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Child"]=df["Premium_Child"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Adult_Individual_Age_21"]=df["Premium_Adult_Individual_Age_21"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Adult_Individual_Age_27"]=df["Premium_Adult_Individual_Age_27"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Adult_Individual_Age_30_"]=df["Premium_Adult_Individual_Age_30_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Adult_Individual_Age_40_"]=df["Premium_Adult_Individual_Age_40_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Adult_Individual_Age_50_"]=df["Premium_Adult_Individual_Age_50_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Adult_Individual_Age_60_"]=df["Premium_Adult_Individual_Age_60_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Couple_21__"]=df["Premium_Couple_21__"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Couple_30_"]=df["Premium_Couple_30_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Couple_40_"]=df["Premium_Couple_40_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Couple_50_"]=df["Premium_Couple_50_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Premium_Couple_60_"]=df["Premium_Couple_60_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_1_child_Age_21"]=df["Couple_1_child_Age_21"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_1_child_Age_30_"]=df["Couple_1_child_Age_30_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_1_child_Age_40_"]=df["Couple_1_child_Age_40_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_1_child_Age_50_"]=df["Couple_1_child_Age_50_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_2_children_Age_21"]=df["Couple_2_children_Age_21"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_2_children_Age_30_"]=df["Couple_2_children_Age_30_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_2_children_Age_40_"]=df["Couple_2_children_Age_40_"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_2_children_Age_50"]=df["Couple_2_children_Age_50"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_3_or_more_Children_Age_21"]=df["Couple_3_or_more_Children_Age_21"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_3_or_more_Children_Age_30"]=df["Couple_3_or_more_Children_Age_30"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_3_or_more_Children_Age_40"]=df["Couple_3_or_more_Children_Age_40"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Couple_3_or_more_Children_Age_50"]=df["Couple_3_or_more_Children_Age_50"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_1_child_Age_21"]=df["Individual_1_child_Age_21"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_1_child_Age_30"]=df["Individual_1_child_Age_30"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_1_child_Age_40"]=df["Individual_1_child_Age_40"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_1_child_Age_50"]=df["Individual_1_child_Age_50"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_2_children_Age_21"]=df["Individual_2_children_Age_21"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_2_children_Age_30"]=df["Individual_2_children_Age_30"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_2_children_Age_40"]=df["Individual_2_children_Age_40"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_2_children_Age_50"]=df["Individual_2_children_Age_50"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_3_or_more_children_Age_21"]=df["Individual_3_or_more_children_Age_21"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_3_or_more_children_Age_30"]=df["Individual_3_or_more_children_Age_30"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_3_or_more_children_Age_40"]=df["Individual_3_or_more_children_Age_40"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Individual_3_or_more_children_Age_50"]=df["Individual_3_or_more_children_Age_50"].replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Standard_On_Exchange"]=df["Standard_On_Exchange"].astype(str)
df["Dental_DeductibleIndividualStandard"]=df["Dental_DeductibleIndividualStandard"].replace('Not Applicable','NaN').replace('See Plan Brochure','NaN').replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Dental_DeductibleFamilyStandard"]=df["Dental_DeductibleFamilyStandard"].replace('Not Applicable','NaN').replace('See Plan Brochure','NaN').replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Dental_DeductibleFamily_(Per_Person)Standard"]=df["Dental_DeductibleFamily_(Per_Person)Standard"].replace('Not Applicable','NaN').replace('See Plan Brochure','NaN').replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Dental_Maximum_Out_of_PocketIndividualStandard"]=df["Dental_Maximum_Out_of_PocketIndividualStandard"].replace('Not Applicable','NaN').replace('See Plan Brochure','NaN').replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Dental_Maximum_Out_of_PocketFamilyStandard"]=df["Dental_Maximum_Out_of_PocketFamilyStandard"].replace('Not Applicable','NaN').replace('See Plan Brochure','NaN').replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Dental_Maximum_Out_of_PocketFamily_(Per_Person)Standard"]=df["Dental_Maximum_Out_of_PocketFamily_(Per_Person)Standard"].replace('Not Applicable','NaN').replace('See Plan Brochure','NaN').replace( '[\$,)]','', regex=True ).replace( '[(]','-', regex=True).astype(float)
df["Routine_Dental_ServicesAdult"]=df["Routine_Dental_ServicesAdult"].astype(str)
df["Basic_Dental_CareAdult"]=df["Basic_Dental_CareAdult"].astype(str)
df["Major_Dental_CareAdult"]=df["Major_Dental_CareAdult"].astype(str)
df["OrthodontiaAdult"]=df["OrthodontiaAdult"].astype(str)
df["Dental_Check-Up_for_Children"]=df["Dental_Check-Up_for_Children"].astype(str)
df["Basic_Dental_CareChild"]=df["Basic_Dental_CareChild"].astype(str)
df["Major_Dental_CareChild"]=df["Major_Dental_CareChild"].astype(str)
df["OrthodontiaChild"]=df["OrthodontiaChild"].astype(str)
#%%
df.to_csv(outfilepath)
print(outfilepath)
