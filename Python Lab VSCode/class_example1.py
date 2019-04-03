class Emp:
    dept = 'Accounts'

    def show(self):
        print('The employee class')

    def show2(self, a, b):    # Self is important ot pass in functions of a class so we have to type it everywhere.
        print(a + b)
    
if __name__ == "__main__":
    e1 = Emp()
    print(e1)
    print(type(e1))
    e1.show()
    e1.show2(1, 2)