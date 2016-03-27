class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise TriangleError
        if a + b <= c or a + c <= b or b + c <= a:
            raise TriangleError
        self.a = a
        self.b = b
        self.c = c

    def kind(self):
        if self.a == self.b == self.c:
            return 'equilateral'
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isosceles'
        if self.a != self.b != self.c:
            return 'scalene'

class TriangleError(Exception):
    pass
