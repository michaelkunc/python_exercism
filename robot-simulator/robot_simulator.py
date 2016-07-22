import operator

NORTH = 'NORTH'
EAST = 'EAST'
SOUTH = 'SOUTH'
WEST = 'WEST'

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot(object):

    def __init__(self, direction=None, coordinate1=None, coordinate2=None):
        self.set_initial_direction(direction)
        self.set_initial_coordinates(coordinate1, coordinate2)

    def set_initial_direction(self, direction=None):
        self.bearing = NORTH
        if direction is not None:
            self.bearing = direction

    def set_initial_coordinates(self, coordinate1=None, coordinate2=None):
        self.coordinates = (0, 0)
        if coordinate1 is not None and coordinate2 is not None:
            self.coordinates = (coordinate1, coordinate2)

    def turn_right(self):
        return self.turn(self.bearing_index(), operator.lt(self.bearing_index(), 3), operator.add(self.bearing_index(), 1), 0)

    def turn_left(self):
        return self.turn(self.bearing_index(), operator.gt(self.bearing_index(), 0), operator.sub(self.bearing_index(), 1), -1)

    def advance(self):
        coordinate1 = self.coordinates[0]
        coordinate2 = self.coordinates[1]
        if self.bearing == NORTH:
            coordinate2 = coordinate2 + 1
        elif self.bearing == EAST:
            coordinate1 = coordinate1 + 1
        elif self.bearing == SOUTH:
            coordinate2 = coordinate2 - 1
        else:
            coordinate1 = coordinate1 - 1
        self.coordinates = (coordinate1, coordinate2)

    def simulate(self, instructions):
        for i in list(instructions):
            self.parse_instruction(i)

    def parse_instruction(self, single_instruction):
        if single_instruction == 'L':
            self.turn_left()
        elif single_instruction == 'R':
            self.turn_right()
        else:
            self.advance()

    def turn(self, current_bearing, lt_gt, add_sub, else_index):
        if lt_gt:
            self.bearing = DIRECTIONS[add_sub]
        else:
            self.bearing = DIRECTIONS[else_index]

    def bearing_index(self):
        return DIRECTIONS.index(self.bearing)
