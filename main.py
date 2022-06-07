import pygame
import random
import cmath
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
    pos = 0 + 0j
    pos.real = random.randint(0, SW)
    pos.imag = random.randint(0, SH)
    return Boid(pos, random.randint(0, 360))

# creates velocity based on rules and applies to boid movement
def moveBoids():
    # Scale variables
    speed = .001
    w1 = 1 * speed
    w2 = 1 * speed
    w3 = 1 * speed

    # stores current boids state to new variable
    # ensures boids only react to previous frame 
    state = boids
    for boid in state:
        
        nearby = getNearbyBoids(boid, state)

        v1 = w1 * flyTowardCenter(boid, state)
        v2 = w2 * keepDistance(boid, nearby)
        v3 = w3 * matchVelocity(boid, nearby)
        boid.velocity = boid.velocity + v1 + v2 + v3
        boid.pos = (boid.pos + boid.velocity)
    
    # # # Wraps boids when they go off screen
    #     boid.pos[1] = boid.pos[1] % np.double(SH)
    #     boid.pos[0] = boid.pos[0] % np.double(SW)

def flyTowardCenter(boid, state):
    c = 0+0j
    for b in state:
        if b is boid:
            continue
        c += b.pos
    if len(state) > 1:
        c /= (len(state) - 1)
    else:
        c = boid.pos
    return (c - boid.pos) / 100

def keepDistance(boid, state):
    c = 0+0j
    for b in state:
        if b is boid:
            continue
        if abs(boid - b) < 100:
            c -= b.pos - boid.pos
    return c

def matchVelocity(boid, state):
    vel = 0+0j
    for b in state:
        if b is boid:
            continue
        vel += b.velocity
    return vel / (len(state) - 1)

def getNearbyBoids(b1, state):
    nearby = []
    for b2 in state:
        if abs(b1.pos - b2.pos) < 300:
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

def main():
    # initialize graphics context and creates array of 100 random boids
    g = Graphics(SW, SH)
    [boids.append(randomBoid()) for _ in range(10)] 
    
    # for i in boids:
    #     i.color = randomColor() 

    # game loop
    start = pygame.time.get_ticks()
    while(pygame.time.get_ticks() - start < 10000):
        
        moveBoids()
        drawBoids(g)
        g.tick(60)

        for event in g.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
        
 
 
if __name__ == "__main__":
    main()
 
sleep(2)
