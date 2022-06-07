import pygame
import cmath
from math import *
 
pygame.init()
 
BLUE = (0, 255, 255)
RED = (255, 0, 0)
 
def getBoidPoints():
    return [complex(3, 0), complex(-1, 1), complex(-1, -1)]
 
def rotate(deg, points: list, origin):
    newPoints = []
    for point in points:
        rotation = complex(cos(radians(deg)), sin(radians(deg)))
        newPoints.append(origin + point * rotation)
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
        pygame.draw.polygon(self.window, boid.color, [(i.real, i.imag) for i in points], 3)
        if flip:
            self.flip()
 
    def flip(self):
        pygame.display.flip()
 
    def tick(self, fr=0):
        self.clock.tick(fr)

    