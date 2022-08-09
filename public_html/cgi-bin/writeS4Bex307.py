#!/usr/bin/python3

# CGI处理模块
import sys, cgi, cgitb 
sys.stderr = sys.stdout


import pandas as pd

def writeData(className,classNo,subject,score):
    records = pd.read_csv('../../DB/dataS4Bex307.csv')
    new_record = {'className':className,'classNo':classNo,'subject':subject,'score':score}
    records = records.append(new_record,ignore_index=True)
    records.to_csv('../../DB/dataS4Bex307.csv', index = False)
    



# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
className = form.getvalue('className')
classNo = form.getvalue('classNo')
subject = form.getvalue('subject')
score = form.getvalue('score')



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
print('<p>班別:',className,'</p>')
print('<p>班內號:',classNo,'</p>')
print('<p>科目:',subject,'</p>')
print('<p>分數:',score,'</p>')
writeData(className,classNo,subject,score)  
print('<h2 class="w3-text-green">資料已被寫入csv檔案中</h2>')
print('</body>')
print('</html>')