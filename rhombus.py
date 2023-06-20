import math
from shape import Shape


class Rhombus(Shape):
    count = 0

    def __init__(self, p, q):
        Rhombus.count += 1
        super().__init__()
        self.p = p
        self.q = q

    def perimeter(self):
        return 4 * (self.side())

    def area(self):
        return (self.p * self.q) / 2

    def side(self):
        return (math.sqrt(self.p ** 2 + self.q ** 2))/2

    def inradius(self):
        try:
            return (self.p * self.q)/(2 * math.sqrt(self.p ** 2 + self.q ** 2))
        except:
            return None

    def print(self):
        perimeter = self.perimeter()
        area = self.area()
        side = self.side()
        inradius = self.inradius()

        formatted_perimeter = f"{perimeter:.5f}" if isinstance(perimeter, float) else 'undefined'
        formatted_area = f"{int(area)}" if isinstance(area, float) else 'undefined'
        formatted_side = f"{side:.5f}" if isinstance(side, float) else 'undefined'
        formatted_inradius = f"{inradius:.5f}" if isinstance(inradius, float) else 'undefined'

        print(
            f"{self.id}: {self.name}, perimeter: {formatted_perimeter},"
            f" area: {formatted_area}, side: {formatted_side},"
            f" inradius: {formatted_inradius}")

    def __eq__(self, other):
        if isinstance(other, Rhombus):
            return self.p == other.p and self.q == other.q
        return False

    def __str__(self):
        return f"{self.name} {self.p} {self.q}"





