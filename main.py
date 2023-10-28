class Human:
    def __init__(self,name = "Human"):
        self.name = name

class Home:
    def __init__(self,brand):
        self.brand = brand
        self.family = []

    def add_family(self, *args):
        for family in args:
            self.family.append(family)

    def print_family_names(self):
        if self.family != []:
            print(f"Сім'я в домі:{self.brand}")
            for family in self.family:
                print(family.name)
        else:
            print(f"в домі{self.brand} сім'я відсутня")

Home = Home("квартира")
for i in range(5):
    p1 = Human(input("Введіть того хто з тобою живе"))
    Home.add_family(p1)

Home.print_family_names()
