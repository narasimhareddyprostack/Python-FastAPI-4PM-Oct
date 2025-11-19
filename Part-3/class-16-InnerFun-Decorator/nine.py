def add(a,b):
    def inner():
        print("Inner")

    return a+b,"Niharika",inner 



result=add(10,20)
print(result)    #30

result[2]()
result[2]()