class Laptop:

    def __init__(self, brand, year, ram, processor):
        # global krna
        self.brand = brand
        self.yr = year
        self.ram = ram
        self.cpu = processor

    def show(self):
        print('Laptop details: ', end = '')
        print(self.brand, end = ' ')
        print(self.yr, end = ' ')
        print(self.ram, end = ' ')
        print(self.cpu)

if __name__ == "__main__":
    new = Laptop('MSI', 2017, '16GB', 'i7 7th gen')
    old = Laptop('Samsung', 2013, '4GB', 'i3 3ed gen')
    old.show()
    new.show()