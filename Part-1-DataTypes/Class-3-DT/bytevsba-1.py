b=bytes([10,20,30,40])
b[0] = 100   
#TypeError: 'bytes' object does not support item assignment
for value in b:
    print(value)

#Bytes - object is Immutable object