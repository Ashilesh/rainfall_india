# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:01:52 2019

@author: Ashilesh
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\data.csv")

df1 = pd.read_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\data.csv")

df2 = pd.read_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\data.csv")

df2.set_index("YEAR",inplace = True)

df1.set_index("SUBDIVISION",inplace = True)

print(df[['YEAR','SUBDIVISION','ANNUAL']])

state = df.SUBDIVISION.unique()
year = df.YEAR.unique()
no = df.SUBDIVISION.nunique(dropna = True)




state = list(state)
year = list(year)

year_1901 = df2.loc[year[0]]

list_1901 = list(year_1901.columns.values)

andman = df1.loc[state[25]]

and_mean = andman['ANNUAL'].mean() / 12

top = list(df1.columns)
