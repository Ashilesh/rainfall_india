import pandas as pd
import os
import numpy as np
from sklearn.linear_model import LinearRegression

def get_rainfall_prediction():
    dir_path = os.getcwd()
    dataset = pd.read_csv(os.path.join(dir_path,'dashboard','dataset','yearly_rainfall.csv'))
    a = list()

    for i in range(2,14):
        y = dataset.iloc[:,i].values
        X = dataset.iloc[:,1].values
        regressor = LinearRegression()
        regressor.fit(X.reshape(-1,1), y.reshape(-1,1))
        pred_year = np.array([2019])
        y_pred = regressor.predict(pred_year.reshape(-1,1))

        a.append(y_pred.tolist())

    m_list = list()

    for i in range(0,12):
        m_list.append(a[i][0][0])

    print(m_list)

    return m_list



def get_state_info(name):
    dir_path = os.getcwd()
    df = pd.read_csv(os.path.join(dir_path,'dashboard','dataset','state_rainfall.csv'))
    data = df.iloc[:,1:]
    row = data[data['state'] == name]

    print(row)
    list_send = row.values.tolist()
    return list_send[0]

def get_quality_dict():
    dir_path = os.getcwd()
    df = pd.read_csv(os.path.join(dir_path,'dashboard','dataset','water_quality.csv'))
    water_dict = df.to_dict('list')
    return water_dict;

def get_chart(year):
    year = int(year)
    dir_path = os.getcwd()
    df = pd.read_csv(os.path.join(dir_path,'dashboard','dataset','yearly_rainfall.csv'))

    data = df.iloc[:,1:]

    row = data[data['YEAR'] == year]

    list_send = row.values.tolist()

    print(list_send)
    print('year is ' + str(year))
    print()
    print()

    return list_send[0]

def get_month(index):
    month = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'Octomber',
    11 : 'November',
    12 : 'December'
    }

    return month[index]

def get_state_raw(code):
    states = {
    'IN-BR' : 'Bihar',
    'IN-DN' : 'Gujarat',
    'IN-DL' : 'Delhi',
    'IN-NL' : 'Nagaland',
    'IN-WB' : 'Bengal',
    'IN-HR' : 'Delhi',
    'IN-HP' : 'Himachal_Pradesh',
    'IN-AS' : 'Assam',
    'IN-UT' : 'Uttaranchal',
    'IN-JH' : 'Jharkhand',
    'IN-JK' : 'Jammu',
    'IN-UP' : 'Uttar_Pradesh',
    'IN-SK' : 'Sikkim',
    'IN-MZ' : 'Nagaland',
    'IN-CT' : 'Chattisgarh',
    'IN-CH' : 'Delhi',
    'IN-GA' : 'Goa',
    'IN-GJ' : 'Gujarat',
    'IN-RJ' : 'Rajsthan',
    'IN-MP' : 'Madhya_Pradesh',
    'IN-OR' : 'Orissa',
    'IN-TN' : 'Tamil_Nadu',
    'IN-AN' : 'Andman',
    'IN-AP' : 'Telangana',
    'IN-TR' : 'Nagaland',
    'IN-AR' : 'Arunachal_Pradesh',
    'IN-KA' : 'Karnataka',
    'IN-PY' : 'Karnataka',
    'IN-PB' : 'Punjab',
    'IN-ML' : 'Assam',
    'IN-MN' : 'Nagaland',
    'IN-MH' : 'Maharashtra',
    'IN-KL' : 'Kerla'
    }

    return states[code]

def get_actual_name(code):
    states = {
    'IN-BR' : 'Bihar',
    'IN-DN' : 'Dadra and Nagar Haveli',
    'IN-PY' : 'Puducherry',
    'IN-DL' : 'Delhi',
    'IN-NL' : 'Nagaland',
    'IN-WB' : 'Bengal',
    'IN-HR' : 'Haryana',
    'IN-HP' : 'Himachal Pradesh',
    'IN-AS' : 'Assam',
    'IN-UT' : 'Uttaranchal',
    'IN-JH' : 'Jharkhand',
    'IN-JK' : 'Jammu and Kashmir',
    'IN-UP' : 'Uttar Pradesh',
    'IN-SK' : 'Sikkim',
    'IN-MZ' : 'Mizoram',
    'IN-CT' : 'Chattisgarh',
    'IN-CH' : 'Chandigarh',
    'IN-GA' : 'Goa',
    'IN-GJ' : 'Gujrat',
    'IN-RJ' : 'Rajsthan',
    'IN-MP' : 'Madhya Pradesh',
    'IN-OR' : 'Orissa',
    'IN-TN' : 'Tamil Nadu',
    'IN-AN' : 'Andman and Nicobar Islands',
    'IN-AP' : 'Andhra Pradesh',
    'IN-TR' : 'Tripura',
    'IN-AR' : 'Arunachal Pradesh',
    'IN-KA' : 'Karnataka',
    'IN-PB' : 'Punjab',
    'IN-ML' : 'Meghalaya',
    'IN-MN' : 'Manipur',
    'IN-MH' : 'Maharashtra',
    'IN-KL' : 'Kerla'
    }

    return states[code]
