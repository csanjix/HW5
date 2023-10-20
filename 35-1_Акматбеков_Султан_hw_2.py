class Figure:
    unit = "cm"

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method.")

    def info(self):
        raise NotImplementedError("Subclasses must implement info method.")


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius * self.__radius

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area()}{self.unit}.")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        print(f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {self.calculate_area()}{self.unit}.")


circles = [Circle(2), Circle(3)]
triangles = [RightTriangle(5, 8), RightTriangle(3, 6), RightTriangle(4, 7)]

for circle in circles:
    circle.info()

for triangle in triangles:
    triangle.info()