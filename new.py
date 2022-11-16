class CoffeCup:
    def __init__(self, temperature):
        self.__temperature = temperature
    def drink_coffe(self):
        if self.__temperature > 85:
            raise NotImplementedError("uegeuegd")
kawa = CoffeCup(90)
kawa.drink_coffe()