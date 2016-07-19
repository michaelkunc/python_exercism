import operator

NORTH = 'NORTH'
EAST = 'EAST'
SOUTH = 'SOUTH'
WEST = 'WEST'

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot(object):

    def __init__(self, direction=None, coordinate1=None, coordinate2=None):
        if direction is None:
            self.bearing = DIRECTIONS[0]
        else:
            self.bearing = direction
        if coordinate1 is None and coordinate2 is None:
            self.coordinates = (0, 0)
        else:
            self.coordinates = (coordinate1, coordinate2)

    def turn_right(self):
        return self.turn(self.bearing_index(), operator.lt(self.bearing_index(), 3), operator.add(self.bearing_index(), 1), 0)

    def turn_left(self):
        return self.turn(self.bearing_index(), operator.gt(self.bearing_index(), 0), operator.sub(self.bearing_index(), 1), -1)

    def advance(self):
        coordinate1 = self.coordinates[0]
        coordinate2 = self.coordinates[1]
        coordinate2 = coordinate2 + 1
        self.coordinates = (coordinate1, coordinate2)


    def turn(self, current_bearing, lt_gt, add_sub, else_index):
        if lt_gt:
            self.bearing = DIRECTIONS[add_sub]
        else:
            self.bearing = DIRECTIONS[else_index]

    def bearing_index(self):
        return DIRECTIONS.index(self.bearing)
