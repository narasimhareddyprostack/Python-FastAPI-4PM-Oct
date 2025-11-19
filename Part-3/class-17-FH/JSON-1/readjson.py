#read json file and print data
#read json file and print all employee names
import json 
fp=open('data.json','r')
emp_data=json.load(fp)
print(emp_data)