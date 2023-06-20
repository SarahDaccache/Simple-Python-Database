import math
from shape import Shape


class Circle(Shape):
    count = 0

    def __init__(self, radius):
        Circle.count += 1
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def print(self):
        perimeter = self.perimeter()
        area = self.area()

        formatted_perimeter = f"{perimeter:.5f}" if isinstance(perimeter, float) else f"{int(perimeter)}"
        formatted_area = f"{area:.5f}" if isinstance(area, float) else f"{int(area)}"

        print(
            f"{self.id}: {self.name}, perimeter: {formatted_perimeter},"
            f" area: {formatted_area}")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __str__(self):
        return f"{self.name} {self.radius}"
