#Write a python script to read emp.json file and 
# print no of male employees
# and   no of female employees

import json 
fp=open('emp.json','r')
employees=json.load(fp)
print("No of employees:-",len(employees))

male_count=0
female_count=0
for emp in employees:
    if emp['gender']=="Male":
        male_count=male_count+1
    elif emp['gender']=="Female":
        female_count=female_count+1


print("No of male Employees:",male_count)
print("No of female Employees:",female_count)
print(fp.closed)
fp.close()
print(fp.closed)