import pandas

data = pandas.read_csv('pc_classroom.csv',encoding='UTF-8')
print(data)
with open('pc_classroom.json', 'w', encoding='utf-8') as file:
    data.to_json(file, orient='records',force_ascii=False)