
class Luhn(object):

    def __init__(self, digit_string):
        self.digit_string = digit_string.replace(' ', '')

    def is_valid(self):
        if len(self.digit_string) < 2 or not self.digit_string.isdigit():
            return False
        else:
            return self.calculate_total() % 10 == 0

    def calculate_total(self):
        total = 0
        for ix, num in enumerate(reversed(self.digit_string)):
            num = int(num)
            if ix % 2 != 0 and num * 2 > 9:
                total += (num * 2) - 9
            elif ix % 2 != 0:
                total += (num * 2)
            else:
                total += num
        return total
