class Allergies(object):

    ALLERGENS = {
        "eggs":         1,
        "peanuts":      2,
        "shellfish":    4,
        "strawberries": 8,
        "tomatoes":     16,
        "chocolate":    32,
        "pollen":       64,
        "cats":         128
    }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, allergen):
        return bool(self.ALLERGENS[allergen] & self.score)

    @property
    def lst(self):
        return list(filter(self.is_allergic_to, self.ALLERGENS))
