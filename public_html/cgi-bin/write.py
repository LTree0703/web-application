data = input('QUERY_STRING:')
new_record = {}
fields = data.split('&')
for field in fields:
    name,value = field.split('=')
    new_record[name]=value  

print(new_record)    