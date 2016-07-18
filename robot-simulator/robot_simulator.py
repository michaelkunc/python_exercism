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
        current_bearing = DIRECTIONS.index(self.bearing)
        return self.turn(current_bearing, operator.lt(current_bearing, 3), operator.add(current_bearing, 1), 0)

    def turn_left(self):
        current_bearing = DIRECTIONS.index(self.bearing)
        return self.turn(current_bearing, operator.gt(current_bearing, 0), operator.sub(current_bearing, 1), -1)

    def turn(self, current_bearing, lt_gt, add_sub, else_index):
        if lt_gt:
            self.bearing = DIRECTIONS[add_sub]
        else:
            self.bearing = DIRECTIONS[else_index]
