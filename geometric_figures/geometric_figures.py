from abc import ABC, abstractmethod
from math import pi, sqrt


class Figure(ABC):
    @abstractmethod
    def area(self, value):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    def __eq__(self, other):
        return self.area == other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area


class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self.radius * 2
        self._area = pi * self.radius**2

    def __str__(self):
        return str(
            f"Koło (promień={self.radius}, średnica={self.diameter}, pole={round(self.area, 2)})"
        )

    def __add__(self, other):
        joint_area = self.area + other.area
        joint_radius = sqrt(joint_area / pi)
        return Circle(joint_radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
            self._diameter = self.radius * 2
            self._area = pi * self.radius**2
        else:
            raise ValueError("Promień nie może być ujemny!")

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = self.diameter / 2
        self._area = pi * self.radius**2

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value > 0:
            self._area = value
            self._radius = sqrt(self.area / pi)
            self._diameter = self._radius / 2


class Square(Figure):
    def __init__(self, side):
        self._side = side
        self._area = side**2

    def __str__(self):
        return str(f"Kwadrat (bok={self.side}, pole={round(self.area, 2)})")

    def __add__(self, other):
        joint_area = self.area + other.area
        joint_side = sqrt(joint_area)
        return Square(joint_side)

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
            self._area = value**2
        else:
            raise ValueError("Bok nie może być ujemny!")

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
        self._side = sqrt(value)


class Triangle(Figure):
    def __init__(self, value):
        self._side = value
        self._area = (value**2 * sqrt(3)) / 4

    def __str__(self):
        return str(f"Trójkąt (bok={self.side}, pole={round(self.area, 2)})")

    def __add__(self, other):
        joint_area = self.area + other.area
        joint_side = sqrt((4 * joint_area) / sqrt(3))
        return Triangle(joint_side)

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
            self._area = (value**2 * sqrt(3)) / 4
        else:
            raise ValueError("Bok nie może być ujemny!")

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
        self._side = sqrt((4 * value) / sqrt(3))
