from random import randint
from math import sqrt
from __future__ import annotations

class Rocket:
    def __init__(self, speed: int = 1, altitude: int = 0, x: int = 0):
        self.altitude = altitude
        self.speed = speed
        self.x = 0

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości: " + str(self.altitude)
    # def get_distance(self, obj2: Rocket):
    #     ac = (self.altitude - obj2.altitude) ** 2
    #     bc = (self.x - obj2.x) ** 2
    #     return sqrt(ac + bc)

class RocketBoard:
    def __init__(self, amountofRockets : int =5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amountofRockets)]
        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].move_up()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]
    def __setitem__(self, key, value):
        self.rockets[key].altitude = value
    @staticmethod
    def get_distance(rocket1: Rocket, rocket2: Rocket):
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return sqrt(ab + bc)
    def __len__(self):
        return len(self.rockets)