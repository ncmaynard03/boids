import pygame
import random
import cmath
from graphics import *
from boid import *
from time import *

# Screen dimensions 
SW, SH = 1300, 700

BLUE = (0, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 100, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# ruleset weights

f = 0
boids = []

def randomColor():
    return random.choice([BLUE, RED, GREEN, WHITE, BLACK])
 
# creates a boid with a random location and direction
def randomBoid():
    pos = complex(random.randint(0, SW), random.randint(0, SH))
    return Boid(pos, random.randint(0, 360))

# creates velocity based on rules and applies to boid movement
def moveBoids():
    mousePos = pygame.mouse.get_pos()
    # Scale variables
    speed = .1
    w1 = 1 * speed
    w2 = 1 * speed
    w3 = 1 * speed
    w4 = 1 * speed
    w5 = 10 * speed

    # stores current boids state to new variable
    # ensures boids only react to previous frame 
    state = boids
    for boid in state:
        
        nearby = getNearbyBoids(boid, state)

        # v1 = w1 * flyTowardCenter(boid, nearby)
        v1 = 0
        v2 = w2 * keepDistance(boid, nearby)
        v3 = w3 * matchVelocity(boid, nearby)
        v4 = w4 * avoidWalls(boid)
        v5 = w5 * followMouse(boid, mousePos)
      
        boid.velocity = limitVelocity(boid.velocity + v1 + v2 + v3 + v4)
        boid.pos += boid.velocity

    # # # Wraps boids when they go off screen
        # boid.pos = complex(boid.pos.real % SW, boid.pos.imag % SH)


def flyTowardCenter(boid, state):
    c = 0+0j

    if len(state) <= 1:
        return c

    for b in state:
        if b is boid:
            continue
        c += b.pos
    c /= (len(state) - 1)
    return (c - boid.pos) / 100


def keepDistance(boid, state):
    c = 0+0j
    for b in state:
        if b is boid:
            continue
        if abs(boid.pos - b.pos) < 15:
            c -= b.pos - boid.pos
        # if boid.pos.real < .1*SW:
        #     c += complex(.1*SW - boid.pos.real, 0)
        # if boid.pos.real > .9*SW:
        #     c += complex(.9*SW - boid.pos.real, 0)
        # if boid.pos.imag < .1*SH:
        #     c += complex(0, .1*SH - boid.pos.imag)
        # if boid.pos.imag < .9*SH:
        #     c += complex(0, .9*SH - boid.pos.imag)
                

    return c

def matchVelocity(boid, state):
    vel = 0+0j
    
    if len(state) <= 1:
        return vel

    for b in state:
        if b is boid:
            continue
        vel += b.velocity
 
    return vel / (len(state) - 1) / 8


def getNearbyBoids(b1, state):
    nearby = []
    for b2 in state:
        if abs(b1.pos - b2.pos) < 150:
            if b1 is not b2:
                nearby.append(b2)
    return nearby

def avoidWalls(boid):
    vel = 0+0j
    r, i = boid.pos.real, boid.pos.imag
    if r < .05 * SW:
        vel += .05 * SW - r
    elif r > .95 * SW:
        vel += .95 * SW - r
    if i < .05 * SH:
        vel += complex(0, .05 * SH - i)
    if i > .95 * SH:
        vel += complex(0, .95 * SH - i)
    return vel

def followMouse(boid, mousePos):
    m = complex(mousePos[0], mousePos[1])
    s = 8
    if abs(boid.pos - m) < 300:
        m/=2
    if abs(boid.pos - m) < 150:
        m/=2
    if abs(boid.pos - m) < 100:
        m/=2
    if abs(boid.pos - m) < 50:
        m/=2
    return m - boid.pos / 4

def limitVelocity(vel):
    if abs(vel) < 10:
        return vel
    scale = 10 / abs(vel)
    return vel * scale



def drawBoids(graphics):
    graphics.window.fill(BLACK)
    [graphics.drawBoid(i) for i in boids]
    graphics.flip()

def main():
    # initialize graphics context and creates array of 100 random boids
    g = Graphics(SW, SH)
    [boids.append(randomBoid()) for _ in range(25)] 
    
    for i in boids:
        i.color = randomColor() 

    # game loop
    # start = pygame.time.get_ticks()
    # while(pygame.time.get_ticks() - start < 10000):
    run = True
    while(run): 
        global f
        f+=1
        moveBoids()
        drawBoids(g)
        g.tick(30)
        for event in g.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
        
 
 
if __name__ == "__main__":
    main()
 
sleep(2)
