from math import pi, sqrt


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
        self.area = pi * self.radius**2

    def __str__(self) -> str:
        return str(
            f"Koło (promień={self.radius}, średnica={self.diameter}, pole={round(self.area, 2)})"
        )
