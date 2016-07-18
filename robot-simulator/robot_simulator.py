NORTH  = 'NORTH'
EAST = 'EAST'
SOUTH = 'SOUTH'
WEST = 'WEST'

class Robot(object):

    def __init__(self, direction=None, coordinate1=None, coordinate2=None):
        if direction is None:
          self.bearing = NORTH
        else:
          self.bearing = direction
        if coordinate1 is None and coordinate2 is None:
          self.coordinates = (0,0)
        else:
          self.coordinates = (coordinate1, coordinate2)
