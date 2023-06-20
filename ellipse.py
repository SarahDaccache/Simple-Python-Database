import math
from shape import Shape


class Ellipse(Shape):
    count = 0

    def __init__(self, a, b):
        Ellipse.count += 1
        super().__init__()
        self.a = max(a, b)
        self.b = min(a, b)

    def area(self):
        return math.pi * self.a * self.b

    def eccentricity(self):
        try:
            c = math.sqrt(self.a ** 2 - self.b ** 2)
            return c
        except:
            return None

    def perimeter(self):
        return None

    def print(self):
        perimeter = self.perimeter()
        area = self.area()
        eccentricity = self.eccentricity()

        formatted_perimeter = f"{perimeter:.5f}" if perimeter is not None and isinstance(perimeter, float) else 'undefined'
        formatted_area = f"{area:.5f}" if area is not None and isinstance(area, float) else 'undefined'
        formatted_eccentricity = f"{eccentricity:.5f}" if eccentricity is not None and isinstance(eccentricity, float) else 'undefined'

        print(
            f"{self.id}: {self.name}, perimeter: {formatted_perimeter}, "
            f"area: {formatted_area}, linear eccentricity: {formatted_eccentricity}"
        )

    def __eq__(self, other):
        if isinstance(other, Ellipse):
            return self.a == other.a and self.b == other.b
        return False

    def __str__(self):
        return f"{self.name} {self.a} {self.b}"
