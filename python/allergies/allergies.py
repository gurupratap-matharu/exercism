class Allergies(object):

    allergies_dict = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats'

    }

    def __init__(self, score):

        self.allergy = [value for key, value in self.allergies_dict.items() if key & score]

    def is_allergic_to(self, item):
        return item in self.allergy

    @property
    def lst(self):
        return self.allergy
