#!/usr/bin/python3
import pandas
import cgi

### 定義寫入數據的函數
csv_path = '../../DB/s5b25ex303Data.csv'


### 由Query String中讀取id
form = cgi.FieldStorage() 
id =  int(form.getvalue('id'))

### 刪除data中id 的資料
data = pandas.read_csv(csv_path,encoding='UTF-8')
data = data[data['id']!=id]
data.to_csv(csv_path,encoding='UTF-8',index=False)

### 向browser輸出json
print("Content-type:application/json")
print()
print('{"result":"ok"}')

