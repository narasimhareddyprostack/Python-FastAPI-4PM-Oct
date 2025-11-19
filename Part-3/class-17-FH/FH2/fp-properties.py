fp=open("Wish.txt",'w')

print(fp.name)        #wish.txt
print(fp.writable())  #True
print(fp.readable())  #False
print(fp.closed)      #False 
fp.close()
print(fp.closed)      #True