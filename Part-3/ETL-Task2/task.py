#Extract - from Rest API
import requests,json,pymongo,csv,mysql.connector
product_resp=requests.get('https://dummyjson.com/products')
product_data=product_resp.json()

products=product_data['products']
print(len(products))


#Transfor - based on requirement
#Load     - into JSON,MongoDB,CSV,Mysql Table