import re

class Phone:
    def __init__(self, number):
        self.handle(number)

    def area_code(self):
        return self.number[0:3]

    def pretty(self):
        return '(' + self.area_code() + ') ' + self.number[3:6] + '-' + self.number[6:10]

    def handle(self, number):
        if re.search(r"^(1?\d{10}|\(\d{3}\) \d{3}\-\d{4}|(\d{3}\.){2}\d{4})$", number):
            number = filter(lambda x: x.isdigit(), number)
            self.number = number if len(number) == 10 else number[1:]
        else:
            self.number = '0000000000'
