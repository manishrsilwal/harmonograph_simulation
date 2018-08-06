import pygame
import sys
import time
import tempfile
from math import pi, sin, cos
from pygame.locals import *
 
#Initialization of graphics library
pygame.init()
p2=1.75
p4=p2/2.0

ax = [-2,2,0]
ay = [2,2,0]
fx = [-1,.99,.5]
fy = [.99,1,.49]
px = [0,p2,0]
py = [p4,0,0]
dd=0.00003
bg=(39, 55, 70)
fg=(242, 65, 27)
inc=0.04
 
# Window size
width = 1024
height = 600
aspect=width/height*2.0
yscale=120
xscale=yscale*aspect
d=0.65
 
screen = pygame.display.set_mode((width, height))
screen.fill(bg)
 
#angle for sine
t=0.0

first=True
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            sys.exit()

# calculate next x,y point along line
    x = xscale * d * (ax[0]*sin(t * fx[0] + px[0]) +
                      ax[1]*sin(t * fx[1] + px[1]) +
                      ax[2]*sin(t * fx[2] + px[2])) + width/2
    y = yscale * d * (ay[0]*cos(t * fy[0] + py[0]) +
                      ay[1]*cos(t * fy[1] + py[1]) +
                      ay[2]*cos(t * fy[2] + py[2])) + height/2
 
    d = d - dd
 
    if not first:
        pygame.draw.aaline(screen, fg, (x, y), (prev_x, prev_y), 2)
    else:
        first=False
 
    prev_x = x
    prev_y = y
 
    pygame.display.update()
    # increment angle for sin
    t+=inc