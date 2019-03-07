a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
c = 11

while c > 4 or c < 1:
    print("1.Addition \n2.Substraction \n3.Multiplication \n4.Division")

    c = int(input("Enter yor choice: "))

    if c == 1:
        d = a + b
    elif c == 2:
        d = a - b
    elif c == 3:
        d = a * b
    elif c == 4:
        d = a / b
    else:
        print("\nWrong Input\n")

print("The answer is: ", d)