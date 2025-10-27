enames=["RG","SG","PG","NM"]
unames=("Rahul","Sonia","Priya")
eids={101,102,103,101,102,103}
ename="Rahul"
bytes_obj=bytes([10,20,30,40])
bytearray_obj=bytearray([10,20,30,40,50])
numbers=range(100)
fz_obj=frozenset({10,10,10,10})

print(20 in fz_obj)                  #False
print("Rahul Gandhi" not in unames)  #True