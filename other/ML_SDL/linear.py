# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:46:37 2019

@author: Ashilesh
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('C:\\Users\\Ashilesh\\Desktop\\ML_SDL\\yearly_rainfall.csv')

a = list()

for i in range(2,14):
    y = dataset.iloc[:,i].values
    X = dataset.iloc[:,1].values
    regressor = LinearRegression()
    regressor.fit(X.reshape(-1,1), y.reshape(-1,1)) 
    pred_year = np.array([2019])
    y_pred = regressor.predict(pred_year)

    a.append(y_pred.tolist())
    
m_list = list()

for i in range(0,12):
    m_list.append(a[i][0][0])    
    



