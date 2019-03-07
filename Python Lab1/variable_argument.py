def avg(*args):
    return sum(args)/len(args)

def reversal(*args):
    for i in args:
        print(i[ : : -1])

def purchases(**kwargs):
    return sum(kwargs.values()), kwargs

if __name__ == "__main__":
    print(avg(1, 2, 3, 4, 5, 6))
    reversal('Hi', 'Hello', 'Woah', 'Good Job', 'Evil')
    print(purchases(tea = 10, coffee = 20, biscuit = 5))