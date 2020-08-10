#%%
# IMPORTING LIBRARIES -------------------------------------
#region
import pandas as pd
import numpy as np
import os
import re
import glob
import csv
import shutil
print('Libs Imported')
#endregion

# READ FILE -----------------------------------------------
#region
print('reading csv file called E.csv in the C drive')
filename = r'C:\e.csv'
df_file = pd.read_csv(filename)                
print('Datafram object generated from csv file')
#endregion

# Delete Unessesary Rows ----------------------------------
#region
print('deleting non PPD rows')
print('')
# String to be searched in start of string  
search_term ="PPD"
# boolean series returned 
Bool_Ser_Filter = df_file["Event name"].str.startswith(search_term)
df_file = df_file[Bool_Ser_Filter]
df_file.reset_index(inplace = True)
#replace blank teachers with 'Unkown, Teacher'
values = {'Teachers': 'Unkown, Teacher'}
df_file.fillna(value=values)
print('deleted')
#endregion

#%%
# LOOP THROUGH
#region
for item in df_file['Teachers']:
    str_teacher = str(item)
    str_teacher = str_teacher.replace(', ', ',')
    lst_teacher = str_teacher.split(',')
    lst_f_names = lst_teacher[0::2]
    lst_l_names = lst_teacher[1::2]
    lst_teacher2 = [i+j for i,j in zip(lst_l_names, lst_teacher[::2])]
    print(lst_teacher2)
#endregion
'''
column_names = df_file.columns
df2 = pd.DataFrame(columns = column_names)
'''
# %%
