#!/usr/bin/python3
import os
import sys, cgi, cgitb # CGI處理模組
import pandas as pd    # pandas 處理csv的模組
from urllib import parse

sys.stderr = sys.stdout #設定錯誤輸出


### 定義寫入數據的函數
csv_path = '../../DB/s5b25ex304Data.csv'

# 將form送上來的資料變換成Dict
data = os.environ['QUERY_STRING']
new_record = {}
fields = data.split('&')
for field in fields:
    name,value = field.split('=')
    new_record[name]=parse.unquote(value)

# 讀寫csv檔案
records = pd.read_csv(csv_path)
records = records.append(new_record, ignore_index=True)
records.to_csv(csv_path, index=False)
    

#########################
##向browser輸出html結果##
#########################
print("Content-type:application/json")
print()
print('{"result":"ok"}')



