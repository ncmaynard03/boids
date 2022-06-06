import pygame
from math import *
 
pygame.init()
 
BLUE = (0, 255, 255)
RED = (255, 0, 0)
 
def getBoidPoints():
    return [(30, 0), (-10, 10), (-10, -10)]
 
def rotate(deg, points: list, origin):
    newPoints = []
    for point in points:
        x, y = point
        rad = sqrt(x**2+y**2)
        theta = radians(degrees(atan2(y, x)) + deg)
        newPoints.append((rad * cos(theta) + origin[0], rad * sin(theta) + origin[1]))
    return newPoints
 
class Graphics:
    def __init__(self, sw, sh):
        self.width = sw
        self.height = sh
        self.window = pygame.display.set_mode((sw, sh))
        self.clock = pygame.time.Clock()
        self.event = pygame.event
 
    def drawBoid(self, boid, flip=False):
        points = rotate(boid.getDirection(), getBoidPoints(), boid.pos)
        pygame.draw.polygon(self.window, boid.color, points, 3)
        if flip:
            self.flip()
 
    def flip(self):
        pygame.display.flip()
 
    def tick(self, fr=0):
        self.clock.tick(fr)

    