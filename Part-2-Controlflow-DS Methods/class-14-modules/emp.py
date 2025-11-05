emp={
    'eid':101,
    'ename':"Rahul",
    'esal':45000
}
#dict.get(key) #retun value of specified key
print(emp.get('eid')) #101
print(emp.get('loc')) #None

for key in emp.keys():
    print(key,":",emp.get(key))