#How to invoke inner function from outside?
def outer():
    print("Outer function started")

    def inner():
        print("Inner Function")
    
    #return 100,200
    return inner

inn=outer()
print(inn)
print(type(inn))
inn()
inn()
inn()
inn()
inn()
inn()




