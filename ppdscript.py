# 1.0 IMPORTING LIBRARIES -------------------------------------------------------------------
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

#region
filename = r'C:\E.xlsx'
Sheet = 'Edval Events'

df_data = pd.read_excel(filename,
                        sheet_name = Sheet)
#endregion
