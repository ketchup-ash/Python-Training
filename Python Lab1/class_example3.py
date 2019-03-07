class Pet:

    def __init__(self, name, age, color, type = 'Dog'):
        self.name = name
        self.age = age
        self.color = color
        self.type = type

    def do_trick(self, trick = 'Flip'):
        print(f'{self.name} is trying to {trick}')

    def eat(self, item = 'Biscuit'):
        print(f'{self.name} eats the {item}')
    
    def speak(self, sound = 'bow bow'):
        print(f'{self.name} does {sound}')

if __name__ == "__main__":
    tommy = Pet('Tommy', 3, 'brown')
    tommy.eat('Pizza')
    tommy.do_trick()
    tommy.speak()

    perry = Pet('Perry', 6, 'Sea green')
    perry.eat()
    perry.speak('grrrrr')
    perry.do_trick('flip')