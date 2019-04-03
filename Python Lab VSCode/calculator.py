class Calculator():

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a // b

    def substract(self, a, b):
        return a - b

if __name__ == "__main__":
    x = int(input('Enter a number:'))   
    y = int(input('Enter second number:'))
    cal = Calculator()

    print(cal.add(x, y))
    print(cal.substract(x, y))
    print(cal.multiply(x, y))
    print(cal.divide(x, y))