from collections import defaultdict

class School:
    def __init__(self, name):
        self.name = name
        self.db = defaultdict(set)

    @property
    def db(self):
        return self.db

    def add(self, name, grade):
        self.db[grade].add(name)

    def grade(self, grade):
        return self.db[grade]

    def sort(self):
        return sorted((grade, tuple(sorted(studs))) for grade, studs in self.db.items())
