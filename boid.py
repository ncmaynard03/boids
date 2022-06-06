from math import *
import numpy as np
 
# Value weights
speedScalar = 3


BLUE = (0, 255, 255)
RED = (255, 50, 50)



def toVelocity(speed, direction):
    theta = radians(direction)
    return np.array([float(speed * cos(theta)), float(speed * sin(theta))])


class Boid:
    #defines from screen position and angle
    def __init__(self, xPos=0, yPos=0, direction=0):
        self.pos = np.array([xPos, yPos]) # position on the screen
        self.velocity = toVelocity(speedScalar, direction)
        self.visibility = 100 # distance
        self.color = RED
 
    # moves boid, rotates to match direction of movement

    def getDirection(self):
        return degrees(np.arctan2(*self.velocity[::-1]))
