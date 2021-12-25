from abc import ABC, abstractmethod

from math import pi, sin, radians

class Geometry(ABC):

    @abstractmethod
    def calc_perimetr(self):
        pass
    @abstractmethod
    def calc_square(self):
        pass

class Cycle(Geometry):

    def __init__(self, radius):
        self.radius = radius

    def calc_perimetr(self):
        return 2 * self.radius * pi

    def calc_square(self):
        return (self.radius ** 2) * pi

class Quadrilateral(Geometry, ABC):

    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    @abstractmethod
    def calc_perimetr(self):
        return self.side1 + self.side2 + self.side3 + self.side4

    @abstractmethod
    def calc_square(self):
        half_perimetr = self.calc_perimetr() / 2
        return ((half_perimetr - self.side1)*(half_perimetr - self.side2)*(half_perimetr - self.side3)
                *(half_perimetr - self.side4))**0.5

class Quadrangle(Quadrilateral):

    def __init__(self, side1, side2):
        super().__init__(side1, side2, side1, side2)

    def calc_square(self):
        return self.side1 * self.side2

    def calc_perimetr(self):
        return super().calc_perimetr()

class Trapezoid(Quadrilateral):
    def __init__(self, side1, osn1, side2, osn2):
        super().__init__(side1, osn1, side2, osn2)

    def calc_perimetr(self):
        return super().calc_perimetr()

    def calc_square(self):
        return super().calc_square()

class Parallelogram(Quadrilateral):
    def __init__(self, side1, side2, angle):
        super().__init__(side1, side2, side1, side2)
        self.angle = angle

    def calc_perimetr(self):
        return super().calc_perimetr()

    def calc_square(self):
        return self.side1 * self.side2 * sin(radians(self.angle))


quadrangle = Quadrangle(2, 2)
print(quadrangle.calc_perimetr())


