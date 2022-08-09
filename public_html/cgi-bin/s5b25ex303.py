import pandas as pd 

data = pd.read_csv('data.csv')
print(data)
'''
indexs = data[data['id']==1].index
data.drop(indexs, inplace=True)
'''

data = data[data['id']!=1]
print(data)
data.to_csv('data.csv',index=False)