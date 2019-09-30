import pandas as pd
import os

def get_chart(year):
    year = int(year)
    dir_path = os.getcwd()
    df = pd.read_csv(dir_path + '\\dashboard\\dataset\\yearly_rainfall.csv')

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
