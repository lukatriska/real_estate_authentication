class Point:
    """
    Represents a point in two-dimensional geometric coordinates
    """

    def __init__(self, x=0, y=0):
        """Initialize the position of a new point. The x and y coordinates can be
        specified. If they are not, the point defaults to the origin."""
        self.move(x, y)

    def move(self, x, y):
        """Move the point to a new location in 2D space."""
        self.x = x
        self.y = y

    def rotate(self, beta, other_point):
        dx = self.x - other_point.get_xposition()
        dy = self.y - other_point.get_yposition()
        beta = radians(beta)
        xpoint3 = dx * cos(beta) - dy * sin(beta)
        ypoint3 = dy * cos(beta) + dx * sin(beta)
        xpoint3 = xpoint3 + other_point.get_xposition()
        ypoint3 = ypoint3 + other_point.get_yposition()
        return self.move(xpoint3, ypoint3)

    def get_xposition(self):
        return self.x

    def get_yposition(self):
        return self.y

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

    def __iadd__(self):
        return self.x + self.y

    def __sub__(self, other_point):
        return Point(self.x - other_point.x, self.y - other_point.y)

    def __isub__(self):
        return self.x - self.y

    def __mul__(self, n):
        return Point(self.x * n.x, self.y * n.y)

    def __imul__(self, n):
        return self.x * self.y

    def __truediv__(self, n):
        return Point(self.x / n.x, self.y / n.y)

    def __itruediv__(self, n):
        return self.x / self.y

    def __floordiv__(self, n):
        return Point(self.x // n.x, self.y // n.y)

    def __ifloordiv__(self, n):
        return self.x // self.y
