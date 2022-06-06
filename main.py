import random
import numpy as np
from graphics import *
from boid import *
from time import *

# Screen dimensions 
SW, SH = 1200, 600

# ruleset weights
w1 = w2 = w3 = 1
 
# creates a boid with a random location and direction
def randomBoid():
    return Boid(random.randint(0, SW), random.randint(0, SH), random.randint(0, 360))

# creates velocity based on rules and applies to boid movement
def moveBoid(boid):
    v1 = w1 * flyTowardCenter()
    v2 = w2 * keepDistance()
    v3 = w3 * matchVelocity()

def flyTowardCenter():
    pass

def keepDistance():
    pass

def matchVelocity():
    pass

def main():
    # initialize graphics context and creates array of 100 random boids
    g = Graphics(SW, SH)
    boids = [randomBoid() for i in range(100)]
    
    # game loop
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        [g.drawBoid(i) for i in boids]
        # [moveBoid(i) for i in boids]
        g.flip()
        g.tick()
 
 
if __name__ == "__main__":
    main()
 
sleep(2)
