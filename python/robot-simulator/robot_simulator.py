NORTH = 1 # up
EAST  = 2 # right
SOUTH = 3 # down
WEST  = 4 # left

class Robot:
    def __init__(self, bearing = NORTH, x = 0, y = 0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    @property
    def bearing(self):
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

    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        else:
            self.bearing = NORTH

    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == EAST:
            self.bearing = NORTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        else:
            self.bearing = SOUTH

    def simulate(self, commands):
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            else:
                self.advance()
