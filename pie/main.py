import math
import pygame
# adapted from https://stackoverflow.com/questions/23246185/python-draw-pie-shapes-with-colour-filled

screen = pygame.display.set_mode((160,160))
screen.fill((125,125,125))
screen_rect = screen.get_rect()
# Center and radius of pie chart
cx, cy = screen_rect.center
r = 75

colors = [[255,0,0],[0,255,0],[0,0,255]]

total = 1
u = 0
divisions = len(colors)
for i in range(1,divisions+1):
    val = total/divisions
# Calculate the angle in degrees
    angle = val*360
    
# Start list of polygon points
    p = [(cx, cy)]

# Get points on arc
    for n in range(u-89,int(angle)+u-89):
        x = cx + int(r*math.cos(n*math.pi/180))
        y = cy + int(r*math.sin(n*math.pi/180))
        p.append((x, y))
    u = int(angle)*i

# Draw pie segment
    if len(p) > 2:
        pygame.draw.polygon(screen, colors[i-1], p)

pygame.display.update()
