from fastapi import FastAPI
app=FastAPI()
'''
usage:Application Root Request
URL:http://127.0.0.1:8000/
Method:GET
Required Fields:None
Access Type Public
'''
@app.get("/")
def index_page():
    return {"message":"Index Page"}

'''
create
------
usage:create new user 
URL:http://127.0.0.1:8000/create
Method Type:POST
Required Fields: uid, uname,loc
Access Type:Public
'''
@app.post("/create")
def create_user():
    print("Inside user create")
    return {"message":"User created Successfully"}


'''
Read
----
usage:fetch all users
URL:http://127.0.0.1:8000/read
Method:GET
Required Fields:None
Access Type:Public
'''
@app.get("/read")
def get_user_details():
    print("inside - get_user_details")
    return {"message":"Fetching user Details"}

'''
update
------
usage:Update user
URL:http://127.0.0.1:8000/update
Method:PUT
Required Fields:None
Access Type:Public
'''
@app.put("/update")
def update_user():
    return {"message":"User Updated Successfully"}

'''
Delete
--------
usage:Delete user 
API URL: http://127.0.0.1:8000/delete
Method : DELETE
Required Fields: None 
Access Type:Public
'''
@app.delete("/delete")
def delete_user():
    return {"message":"User Deleted Successfully!"}
