# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:02:01 2019

@author: Ashilesh
"""

import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')


df = pd.read_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\data.csv")

states = list(df.SUBDIVISION.unique())
columns = list(df.columns.values)

dictionary = dict()

for column in range(2,14):
    dictionary[columns[column]] = []

dictionary['avg_year'] = []
dictionary['min_value_year'] = []
dictionary['min_year'] =[]
dictionary['max_value_year'] = []
dictionary['max_year'] = []
dictionary['total_rainfall'] = []
dictionary['state'] = []

for state in states:
    mf = df[df['SUBDIVISION'] == state]
    # taking care of nan values
    data_impute = mf.iloc[:,:].values
    data_impute[:,2:] = imputer.fit_transform(data_impute[:,2:])
    mf = pd.DataFrame(data_impute)
    mf.columns = columns
  
    
    for month in range(2,14):
        dictionary[columns[month]].append(mf[columns[month]].mean())
    
    dictionary['avg_year'].append(mf['ANNUAL'].mean())
    
    dictionary['min_value_year'].append(min(mf['ANNUAL']))
    
    li = list(mf['ANNUAL'])
    
    min_year = mf.iloc[li.index(min(li)),1]
    
    dictionary['min_year'].append(min_year)
    
    # max year
    dictionary['max_value_year'].append(max(mf['ANNUAL']))
    
    max_year = mf.iloc[li.index(max(li)),1]
    
    dictionary['max_year'].append(max_year)
    
    dictionary['total_rainfall'].append(sum(mf['ANNUAL']))
    
    dictionary['state'].append(state)
    
mf = pd.DataFrame(dictionary)
    
mf.to_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\state_rainfall_DEMO.csv")