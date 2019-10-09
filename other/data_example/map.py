# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:19:26 2019

@author: Ashilesh
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\data.csv")

states = list(df.SUBDIVISION.unique())

state_df = df[df['SUBDIVISION'] == states[0]]

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')

state_impute = state_df.iloc[:,:].values

state_impute[:,1:] = imputer.fit_transform(state_impute[:,1:])

state_impute = pd.DataFrame(state_impute)

header = list(df.columns.values)

no = header.index('ANNUAL')


df1 = pd.read_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\water_dataX.csv")

with open("C:\\Users\\Ashilesh\\Desktop\\data_example\\water_dataX.csv", 'r', newline='\n') as c:
    ff = pd.read_csv(c)

list_state = list(ff.year.unique())
ff = ff.replace('', np.nan, regex=True)

year = list(ff.year.unique())

columns_name = list(ff.columns.values)

ff_impute = ff.iloc[:,:].values

ff_impute[:,3:] = imputer.fit_transform(ff_impute[:,3:])

ff_impute = pd.DataFrame(ff_impute)

my_dict = dict()
for l in range(3,13):
    my_dict[csv_column[l]] = []
    
ff_impute.columns = ['STATION_CODE','LOCATION','STATE',\
                     'TEMP','DO','PH','CONDUCTIVITY','BOD','NITRITE',\
                     'FECAL_COLIFORM','TOTAL_COLIFORM','YEAR']

csv_column = ['STATION_CODE','LOCATION','STATE',\
                     'TEMP','DO','PH','CONDUCTIVITY','BOD','NITRITE',\
                     'FECAL_COLIFORM','TOTAL_COLIFORM','YEAR']

year = ff_impute.YEAR.unique()

print(ff_impute['FECAL_COLIFORM'].add())

for y in year:
    mf = ff_impute[ff_impute['YEAR'] == y]
    for i in range(3,12):
        my_dict[csv_column[i]].append(mf[csv_column[i]].mean())
        print(i)
        
vd = pd.DataFrame(my_dict)
    
vd.to_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\water_quality.csv",index = False)
    