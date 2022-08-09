import pandas

data = pandas.read_csv('taobao.csv',encoding='UTF-8')
data.to_json('taobao2.json', orient='records',force_ascii=False)
