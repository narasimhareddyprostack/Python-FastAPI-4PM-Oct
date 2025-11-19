from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    user_col=db['users']
    user_col.insert_one({"uid":101,"uname":"Rahul"})
    print("Document Inserted Successfully!")

except:
    print("Unable to Insert")

finally:
    pass