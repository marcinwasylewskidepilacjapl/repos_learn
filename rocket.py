from random import randint

class Rocket:
    def __init__(self, speed=1):
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed

    # def __str__(self):
    #     return "Rakieta jest aktualnie na wysokości: " + str(self.altitude)
    def get_distance(self, rocket):
        return abs(rocket.altitude - self.altitude)
    def get_all_chosen_rockets_distances(self,*rocket):
        all_chosen_rockets_distances = 0
        for i in rocket:
            print(i.altitude)
            all_chosen_rockets_distances += i.altitude
        return all_chosen_rockets_distances+self.altitude
class RocketBoard:
    def __init__(self, amountofRockets=5):
        self.rockets = [Rocket(randint(1, 10)) for _ in range(amountofRockets)]
        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]
    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

