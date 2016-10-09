

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot(object):

    def __init__(self, direction=NORTH, x=0, y=0):
        self.bearing = direction
        self.x = x
        self.y = y

    def turn_right(self):
        self.bearing = DIRECTIONS[(self.bearing + 1) % 4]
        return self.bearing

    def turn_left(self):
        self.bearing = DIRECTIONS[(self.bearing - 1) % 4]
        return self.bearing

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        else:
            self.x -= 1

    def simulate(self, instructions):
        for i in list(instructions):
            if i == 'L':
                self.turn_left()
            elif i == 'R':
                self.turn_right()
            else:
                self.advance()

    @property
    def coordinates(self):
        return (self.x, self.y)
