from math import *
 
# Value weights
speedScalar = 1
 
 
class Boid:
    #defines from screen position and angle
    def __init__(self, xPos=0, yPos=0, direction=0):
        self.pos = (xPos, yPos) # position on the screen
        self.dir = direction # between 0-360, CCW from 3:00
        self.visibility = 100 # distance
 
    # moves boid, rotates to match direction of movement
    def move(self, dx, dy):
        self.dir = atan2(dy, dx)
        x, y = self.pos
        self.pos = (x + dx, y + dy)
