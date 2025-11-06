#read data.txt file and 
#write data into new file ie wish.txt file
fp=open('wish.txt','w')
data='''
     Dear Rahul,
     I miss you
     '''
fp.write(data)
print("New File created successfully")
fp.close()