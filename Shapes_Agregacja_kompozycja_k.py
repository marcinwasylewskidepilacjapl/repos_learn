class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def count_surface_area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, side_Length):
        super().__init__(side_Length, side_Length)
class Cube():
    def __init__(self, square):
        self.square = square
        self.height = square.height
    def count_surface_area(self):
        return super().count_surface_area() * 6
    def count_volume(self):
        return super().count_surface_area() * self.height
class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height
    def count_volume(self):
        return self.base._count_surface_area() * self.height

    def count_surface_cuboid(self):
        return 2*self.base.count_surface_area() + (2*self.base.width + 2*self.base.height)*self.height
cuboid = Cuboid(Rectangle(2,3), 4)

print(cuboid.count_surface_cuboid())
