#How to invoke inner function from outside?
def outer():
    print("Outer function started")

    def inner():
        print("Inner Function")

outer()
inner()  #NameError