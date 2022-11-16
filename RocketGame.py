import random
import time
class Fly_Machine:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def moving_up(self):
        self.move_up = 1
        return self.move_up
    def power_up(self):
        power = random.randint(0, 10)
        self.power = power
        return self.power
    def crash(self):
        self.power = 0
    def fly(self):
        self.fly_power = self.moving_up() * self.power_up()
        return self.fly_power
    def current_distance(self):
        try:
            self.current_distance_1 += self.fly()
        except:
            self.current_distance_1 = 0
        finally:
            return self.current_distance_1

class Aeroplane(Fly_Machine):
    def __init__(self,name, country, passengers):
        # super(Aeroplane,self).__init__(name=name, country=country)
        self.passengers = passengers
class Rocket(Fly_Machine):
    pass
def Print_machines(Machine_dict):
    for i in Machine_dict:
        print(i, Machine_dict[i])

if __name__ == '__main__':
    Machine_dict = {}
    Turn_on = True
    while Turn_on == True:
        print("1 - Utwórz nowa maszyne latającą")
        print("2 - Zepsuj maszynę")
        print("3 - Sprawdz aktualny dystans maszyny")
        print("4 - Wyświetl maszyny")
        choice = int(input())
        if choice == 1:
            print("Podaj nazwe maszyny")
            name = input()
            print("Podaj kraj pochodzenia")
            country = input()
            nazwamaszyny = name + country
            print("Samolot czy Rakieta? S/R")
            choice2 = input()
            choice2.capitalize()
            if choice2 == "S":
                Machine_dict[nazwamaszyny] = Aeroplane(name,country, passengers=120)
                a =1
            else:
                Machine_dict[nazwamaszyny] = Rocket(name,country)
        if choice == 3:
            for i in Machine_dict:
                print(i, Machine_dict[i].current_distance())
        if choice == 4:
            Print_machines(Machine_dict)
    # Rocket1.fly()
