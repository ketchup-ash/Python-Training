# Fuction Type:
#     1. Parameterized
#     2. With return Value
#     3. Default parameters
#     4. Variable parameters
#     5. lambda expressions

import math

def factor(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    print(f'Factors of {number} are {factors}\n')

def pythagoras(x, y):
    hyp = math.sqrt(x**2 + y**2)
    return hyp

if __name__ == "__main__":
    factor(int(input('Enter a number:')))

    x = int(input('Enter a number:'))
    y = int(input('Enter a number:'))

    result = pythagoras(x, y)
    print(f'Hypetnues of {x} and {y} is {result}')