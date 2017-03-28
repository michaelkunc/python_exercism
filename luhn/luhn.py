
class Luhn(object):

    def __init__(self, id_string):
        self.id_string = id_string.replace(' ', '')

    def is_valid(self):
        if len(self.id_string) < 2 or not self.id_string.isdigit():
            return False
        else:
            total = 0
            for ix, num in enumerate(reversed(self.id_string)):
                num = int(num)
                if ix % 2 != 0 and num * 2 > 9:
                    total += (num * 2) - 9
                elif ix % 2 != 0:
                    total += (num * 2)
                else:
                    total += num
        return total % 10 == 0
