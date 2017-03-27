
class Luhn(object):

    def __init__(self, id_string):
        self.id_string = id_string.replace(' ', '')

    def is_valid(self):
        container = []
        if len(self.id_string) < 2 or any(s.isalpha() for s in self.id_string):
            return False
        else:
            for ix, num in enumerate(reversed(self.id_string)):
                num = int(num)
                if ix % 2 != 0:
                    if num * 2 > 9:
                        container.append((num * 2) - 9)
                    else:
                        container.append(num * 2)
                else:
                    container.append(num)
        return sum(container) % 10 == 0
