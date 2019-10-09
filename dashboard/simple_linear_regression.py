# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:15:52 2019

@author: Ashilesh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing dataset
dataset = pd.read_csv('yearly_rainfall.csv')

# X is matrix of features
X = dataset.iloc[:,:-1].values
# y is vector
y = dataset.iloc[:,-1].values

# creating training and testing dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# no need of feature scaling library will do this for us

# fitting simple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting the test set results
y_pred = regressor.predict(X_test)

# visualising training set result
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_test, y_pred, color = 'blue')
plt.scatter(X_test, y_test, color = 'green')
plt.title('Experience vs Salary')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
