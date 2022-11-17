class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area = 0
    def Area(self):
        self.area = self.a * self.b
        return self.area
    def __str__(self):
        return "Boki mają wartosci " + str(self.a) + ", " + str(self.b) + "\nPole powierzchni " + str(self.area) + "\n"
class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
    def __str__(self):
        return "Bok a wynosi " + str(self.a) + "\nPole powierzchni " + str(self.area) + "\n"
class Cube(Square):
    def CubeArea(self):
        self.cube_area = 6 * super().Area()
        return self.cube_area
    def Volume(self):
        self.volume = super().Area() * self.a
        return self.volume
    def __str__(self):
        return "Bok a wynosi " + str(self.a) + "\nJedna ściana ma powierzchnię " + str(self.area) +"\nPole sześcianu wynosi " + str(self.cube_area) + "\nObjętość wynosi " + str(self.volume) + "\n"
sześcian = Cube(2)
sześcian.CubeArea()
sześcian.Volume()
print(sześcian)
kwadrat = Square(4)
kwadrat.Area()
print(kwadrat)
prostokąt = Rectangle(3,4)
prostokąt.Area()
print(prostokąt)