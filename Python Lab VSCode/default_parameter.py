def adder(a = 1, b = 2, c = 3):
    return a + b + c

if __name__ == "__main__":    
    print(f'Result is {adder()}')
    print(f'Result is {adder(10, c = 4)}')