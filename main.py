from pickle import REDUCE
import pygame
import random
import numpy as np
from graphics import *
from boid import *
from time import *

# Screen dimensions 
SW, SH = 1200, 600

BLUE = (0, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 100, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ruleset weights


boids = []

def randomColor():
    return random.choice([BLUE, RED, GREEN, WHITE, BLACK])
 
# creates a boid with a random location and direction
def randomBoid():
    return Boid(random.randint(0, SW), random.randint(0, SH), random.randint(0, 360))

# creates velocity based on rules and applies to boid movement
def moveBoid(boid):
    w1 = .00005
    w2 = 1
    w3 = 1
    v1 = w1 * flyTowardCenter(boid)
    # v2 = w2 * keepDistance(boid)
    matchVelocity(boid)
    boid.velocity = boid.velocity + v1
    boid.pos = boid.pos + boid.velocity
    
    # Wraps boids when they go off screen
    boid.pos[0] %= SW
    boid.pos[1] %= SH

def flyTowardCenter(boid):
    total = np.array([0,0])
    for b in getNearbyBoids(boid):
        if b is not boid:
                total = total + b.pos
    center = total / (len(boids) - 1)
    return boid.pos - center

def keepDistance(boid):
    pass

def matchVelocity(boid):
    pass

def getNearbyBoids(b1):
    nearby = []
    for b2 in boids:
        if getDistance(b1.pos, b2.pos) < 300:
            if b1 is not b2:
                nearby.append(b2)
    return nearby

def getDistance(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def drawBoids(graphics):
    graphics.window.fill(BLACK)
    [graphics.drawBoid(i) for i in boids]
    graphics.flip()
    graphics.tick(120)

def main():
    # initialize graphics context and creates array of 100 random boids
    g = Graphics(SW, SH)
    [boids.append(randomBoid()) for _ in range(10)] 
    for i in boids:
        i.color = randomColor() 
    
    # game loop
    start = pygame.time.get_ticks()
    while(pygame.time.get_ticks() - start < 5000):
        
        [moveBoid(i) for i in boids]
        drawBoids(g)

        for event in g.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

                exit()
        
 
 
if __name__ == "__main__":
    main()
 
sleep(2)
