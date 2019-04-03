def pattern(symbol = '*', size = 5):
    for i in range(size):
        print(symbol * i)

def surprise(size = 5):
    for i in range(-size + 1, size):
        for j in range(-size + 1, size):
            if i < 0:
                i *= -1
            if j < 0:
                j *= -1
            
            if i > j:
                print(i + 1, end = '  ')
            else:
                print(j + 1, end = '  ')
        print('\n')

if __name__ == "__main__":
    # pattern()
    # pattern('-')
    # pattern('o', 15)
    # pattern('k', 7)

    surprise()