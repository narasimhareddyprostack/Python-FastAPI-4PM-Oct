import requests,json 
fp=open('user.json','w')
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp_data.json()

json.dump(users,fp)
print("New File Created Successfully!")

fp.close()