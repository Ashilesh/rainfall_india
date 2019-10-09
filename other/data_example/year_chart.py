# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:53:02 2019

@author: Ashilesh
"""

import pandas as pd

def create_csv_year():
    df = pd.read_csv("C:\\Users\\Ashilesh\\Desktop\\data_example\\data.csv")
    years = list(df.YEAR.unique())
    columns_list = list(df.columns.values)
        
    my_dict = dict()
    
    my_dict = initialize_dictionary(my_dict,columns_list)
    
    
"""
    my_dict[columns_list[1]] = [400,2300,300]
    
    print(my_dict[columns_list[0]].append(5))
    
    for year in years:
        year = df.loc[year]
        mean_jan = df[columns_list[2]].mean()
"""   

def initialize_dictionary(u_dict,u_list):
    for l in range(1,15):
        u_dict[u_list[l]] = []
    
    return u_dict;
    
create_csv_year()