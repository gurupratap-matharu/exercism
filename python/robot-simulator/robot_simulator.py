# Globals for the bearings
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):

        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):

        i = directions.index(self.bearing) + 1
        i %= 4 # to turn from west to north
        self.bearing = directions[i]

    def turn_left(self):

        i = directions.index(self.bearing) - 1
        i %= 4 # to turn from west to north
        self.bearing = directions[i]

    def advance(self):
        x, y = self.coordinates
        if self.bearing == 'NORTH':
            y += 1
        elif self.bearing == 'EAST':
            x += 1
        elif self.bearing == 'SOUTH':
            y -= 1
        else:
            x -= 1
        self.coordinates = (x, y)

    def simulate(self, commands):
        for command in list(commands):
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            else:
                self.advance()
