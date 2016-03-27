class Matrix:
    def __init__(self, numbers):
        self.matrix = [map(int, line.split(' ')) for line in numbers.split('\n')]

    @property
    def rows(self):
        return self.matrix

    @property
    def columns(self):
        return map(list, zip(*self.matrix))
