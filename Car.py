from random import randint

class car:
    next_id = 1
    def __init__(self, speed: int = 1):
        self.distance = 0
        self.speed = speed
        self.car_id = car.next_id
        car.next_id += 1
    def road_distance(self):
        self.distance += self.speed
    def __str__(self) -> str:
        return "Auto jest na dystansie " + str(self.distance)
class race_track:
    def __init__(self, amountofCars: int = 1):
        self.amountofCars = amountofCars
        self.racetrack = [car(randint(1,20)) for _ in range(self.amountofCars)]
    def race(self):
        self.Stop = False
        for i in range(self.amountofCars):
            IndexRacingCar = randint(0, len(self.racetrack)-1)
            self.racetrack[IndexRacingCar].road_distance()
            print("nr", IndexRacingCar, ":", self.racetrack[IndexRacingCar])
            if self.racetrack[IndexRacingCar].distance >= 100:
                print("Koniec wyścigu!!! Auto z nr", IndexRacingCar, "wygrywa!!!")
                self.Stop = True
                break
    def __getitem__(self, key) -> int:
        return self.racetrack[key].distance
    def __setitem__(self, key, value):
        self.racetrack[key].distance = value


grandPrix = race_track(6)
for _ in range(50):
    grandPrix.race()
    if grandPrix.Stop == True:
        break
print("przyklad uzycia metody dunder getitem do wyswietlenia dowolnego dystansu samochodu ", grandPrix[randint(0,5)])
print("przyklad uzycia metody dunder getitem do wyswietlenia dystansu samochodu ostatniego z listy", grandPrix[-1])
grandPrix[-1] = 600
print("przyklad uzycia metody dunder setitem do ustalenia dystansu samochodu ostatniego z listy", grandPrix[-1])
print("przyklad uzycia metody dunder getitem do wyswietlenia dowolnego dystansu samochodu ", grandPrix[-1])
print(grandPrix.racetrack)
for i in grandPrix.racetrack:
    print(i.car_id)
