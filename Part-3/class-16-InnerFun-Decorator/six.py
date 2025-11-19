def calc():
    print('Outer function started')

    def add():
        print("Addition")
    
    def multi():
        print("Multiplication")

    return add,multi

inner=calc()
print(type(inner))
inner[0]()
inner[0]()
inner[1]()