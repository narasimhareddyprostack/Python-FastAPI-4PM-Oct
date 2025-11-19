import json
fp1=open("data.json",'r')
fp2=open("emp.json",'w')

employees=json.load(fp1)
print(employees)
json.dump(employees,fp2)
print("New Json File created successfully!")

fp1.close()
fp2.close()