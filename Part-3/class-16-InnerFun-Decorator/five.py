def calc():
    print('Outer function started')

    def add():
        print("Addition")
    
    def multi():
        print("Multiplication")

    return add 

inner=calc()
inner()
inner()