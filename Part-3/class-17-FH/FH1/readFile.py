#read data.txt file and print file data
fp=open('data.txt','r')
data=fp.read()
print(data)
fp.close()