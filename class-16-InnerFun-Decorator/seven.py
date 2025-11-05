def outer():
    def f1():
        print("Inner Function 1")
    def f2():
        print("Inner Function 2")
    def f3():
        print("Inner Function 3")

    return f1,f2,f3

result = outer()

print(result)          #(f1,f2,f3)
print(result[0])       #f1
print(result[1])       #f2
print(result[2])       #f3


result[2]()
result[2]()
result[2]()