import random as r
from string import ascii_uppercase as upper


class Robot(object):
    count = 0

    def __init__(self):
        self.name = self.create_name()
        self.__class__.count += 1

    def create_name(self):
        r.seed(self.__class__.count)
        letters = r.sample(upper, 2)
        numbers = r.sample(range(0, 9), 3)
        return ''.join(letters + [str(i) for i in numbers])

    def reset(self):
        self.name = self.create_name()
