PLANTS = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}

STUDENTS = [
    'Alice',
    'Bob',
    'Charlie',
    'David',
    'Eve',
    'Fred',
    'Ginny',
    'Harriet',
    'Ileana',
    'Joseph',
    'Kincaid',
    'Larry'
]

class Garden:
    def __init__(self, plants, students = STUDENTS):
        self.one, self.two = plants.split('\n')
        self.students = sorted(students)

    def plants(self, name):
        return [PLANTS[self.one[self.students.index(name) * 2]], PLANTS[self.one[self.students.index(name) * 2 + 1]], PLANTS[self.two[self.students.index(name) * 2]], PLANTS[self.two[self.students.index(name) * 2 + 1]]]
