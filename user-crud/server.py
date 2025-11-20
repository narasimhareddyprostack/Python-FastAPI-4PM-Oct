from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
users=[]
class User(BaseModel):
    uid:int
    uname:str 
    loc:str 

'''
create
------
usage:create new user
API URL:http://127.0.0.1:8000/create
Method Type:POST
Required Fields: uid,uname,loc
Access Type:Public
'''
@app.post("/create")
def create_user(user:User):
    print(user)
    users.append(user)
    return {"message":"New User created Successfully"}

'''
read
-----
usage: fetch all users 
api URL: http://127.0.0.1:8000/read
Method Type:GET
Required Fields:None 
Access Type:Public
'''
@app.get("/read")
def get_users():
    return users