
class Allergies:
    allergens = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8,
                 'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128}

    def __init__(self, score):
        self.score = score
        self.list = self.allergen_list()

    def allergen_list(self):
        return sorted([x for x in self.allergens if self.is_allergic_to(x)], key=lambda i: self.allergens[i])

    def is_allergic_to(self, allergen):
        return self.allergens[allergen] & self.score
