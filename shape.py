class Shape:
    count = 0

    def __init__(self):
        Shape.count += 1
        self.id = Shape.count
        self.name = self.__class__.__name__

    def perimeter(self):
        return None

    def area(self):
        return None

    def print(self):
        perimeter = self.perimeter()
        area = self.area()

        print(
            f"{self.id}: {self.name}, perimeter: {perimeter if perimeter is not None else 'undefined'}, "
            f"area: {area if area is not None else 'undefined'}")

    def __eq__(self, other):
       return isinstance(other, self.__class__)

    def __str__(self):
        return self.name

