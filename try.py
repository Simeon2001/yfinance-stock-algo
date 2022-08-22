from ast import Lambda
from random import triangular
import pandas as pd
from functools import reduce
data = pd.read_csv("task3.csv")
#data['color'] = (data['close']) > (data['open'])
#data['color'] = data.color.map({True:"green", False:"red"})
#print(data.isnull().sum())
#print(data.head())

#datas = data[["open","high"]]
#print(datas)

data['0'] = data['0'].fillna((data['0'].mean()))
data['1'] = data['1'].fillna((data['1'].mean()))

#print(data['0'] , data['1'])
print(data.head())
triggers_in_datetime = []
t = 0
s1 = list(data['0'])
s2 = list(data['1'])
for value_one, _ in enumerate(zip(s1,s2)):
    if s1[value_one] < s2[value_one]:
        triggers_in_datetime.append(data.iloc[value_one,:]['Datetime'])
print(triggers_in_datetime)
            





#if data['0'] > data['1']:
#    print(len(data['0']))