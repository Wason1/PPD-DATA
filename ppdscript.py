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
df_file.reset_index(inplace = True, drop = True)
#replace blank teachers with 'Unkown, Teacher'
values = {'Teachers': 'Unkown, Teacher'}
df_file = df_file.fillna(value=values)
print('deleted')
#endregion

#%%
# LOOP THROUGH
#region
row_number = 0
df_out = pd.DataFrame(columns= df_file.columns)
for item in df_file['Teachers']:
    str_teacher = str(item)
    str_teacher = str_teacher.replace(', ', ',')
    lst_teacher = str_teacher.split(',')
    lst_f_names = lst_teacher[0::2]
    lst_l_names = lst_teacher[1::2]
    lst_teacher2 = [i+', '+j for i,j in zip(lst_f_names, lst_l_names)]
    for ateacher in lst_teacher2:
        new_row = df_file.iloc[row_number]
        new_row.iloc[7] = ateacher
        df_out = df_out.append(new_row)
    row_number += 1
df_out.reset_index(inplace = True, drop = True)
print('ALL DONE')
        
#endregion


# %%
