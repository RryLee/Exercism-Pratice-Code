class Allergies:
    foods = ['eggs','peanuts','shellfish','strawberries',
             'tomatoes','chocolate','pollen','cats']

    def __init__(self, score):
        self.score = score
        self.lst = self.getList()

    def is_allergic_to(self, food):
        return self.score & 1 << self.foods.index(food)

    def getList(self):
        return [food for food in self.foods if self.is_allergic_to(food)]
