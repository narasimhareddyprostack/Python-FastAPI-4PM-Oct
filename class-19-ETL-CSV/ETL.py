import requests,json,csv 
fp1=open("emp.json",'w')
fp2=open('emp.csv','w',newline="")
#Extract Data from Rest API
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=user_resp.json()
status_code =user_resp.status_code
print(users)
print(status_code)