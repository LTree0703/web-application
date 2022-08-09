#!/usr/bin/python3

import sys, cgi, cgitb # CGI處理模組
import pandas as pd    # pandas 處理csv的模組

sys.stderr = sys.stdout #設定錯誤輸出


### 定義寫入數據的函數
def writeData(Telno, Food, Shipping):
    records = pd.read_csv('../../DB/s5b25ex202Data.csv')
    new_record = {'Telno':Telno,'Food':Food, 'Shipping':Shipping}
    records = records.append(new_record,ignore_index=True)
    records.to_csv('../../DB/s5b25ex202Data.csv', index=False)
    

# 創建讀取 form 送上來的數據的實體
form = cgi.FieldStorage() 

# 獲取form送上來的資料
Telno = form.getvalue('Telno')
Food = form.getvalue('Food')
Shipping = form.getvalue('Shipping')

# 呼叫writeData函數, 將資料寫入csv檔案中
writeData(Telno, Food, Shipping) 



#########################
##向browser輸出html結果##
#########################
print("Content-type:text/html")
print()
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>python cgi-bin 程序</title>')
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3pro.css">')
print('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">') 
print('</head>')
print('<body>')
print('<h1 class="w3-red">接收到的資料</h1>')
print('<p>電話號碼:',Telno,'</p>')
print('<p>食物:',Food,'</p>')  
print('<p>配送方式:',Shipping,'</p>')  
print('<h2 class="w3-green">資料已被寫入csv檔案中</h2>')
print('</body>')
print('</html>')