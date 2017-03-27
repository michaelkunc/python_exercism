class Luhn(object):

    def __init__(self, id_string):
        self.id_string = int(id_string.replace(' ', ''))

    def is_valid(self):
        if self.id_string < 2:
            return False
        else:
            return True
