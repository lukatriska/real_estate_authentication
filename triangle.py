from point import Point


class Triangle:

    def __init__(self, vertex_1, vertex_2, vertex_3):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.vertex_3 = vertex_3
        self.side1 = ((Point(self.vertex_1, self.vertex_2).__iadd__()) ** 2 +
                      (Point(self.vertex_1, self.vertex_2).__iadd__()) ** 2) ** 0.5
        self.side2 = ((Point(self.vertex_1, self.vertex_3).__iadd__()) ** 2 +
                      (Point(self.vertex_1, self.vertex_3).__iadd__()) ** 2) ** 0.5
        self.side3 = ((Point(self.vertex_2, self.vertex_3).__iadd__()) ** 2 +
                      (Point(self.vertex_2, self.vertex_3).__iadd__()) ** 2) ** 0.5

    def is_triangle(self):
        """
        () -> bool

        Returns True if, based on the three given coordinates, it is a triangle.
        """
        return True if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and \
                       self.side2 + self.side3 > self.side1 else False

    def perimeter(self):
        """
        () -> number

        Returns the perimeter of a given triangle.
        """
        return self.side1 + self.side2 + self.side3

    def area(self):
        """
        () -> number

        Returns the area of a given triangle.
        """
        return ((self.perimeter() / 2) * ((self.perimeter() / 2) - self.side1) *
                ((self.perimeter() / 2) - self.side2) * ((self.perimeter() / 2) - self.side3)) ** 0.5
