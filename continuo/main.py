from resources import *
import pygame,sys

pygame.init()
ancho,alto = 640, 480
fondo = pygame.display.set_mode([ancho, alto])
canvas = fondo.copy()
rect = canvas.get_rect()
FPS = pygame.time.Clock()

textura = pygame.image.load('pasto5.png')
for y in range(alto//32):
    y *= 32
    for x in range(ancho//32):
        x *= 32
        canvas.blit(textura,(x,y))

#heroe = mob(32,32)
#update = pygame.sprite.LayeredDirty(heroe)
dx,dy = 0,0
while True:
    #dx,dy = 0,0
    #fondo.fill((0,0,0))
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_DOWN:
                dy = -1
                y = alto+dy*32
                for x in range(ancho//32):
                    fondo.blit(textura,(x,y))
            if event.key == pygame.K_UP:
                dy = 1
            if event.key == pygame.K_RIGHT:
                dx = -1
            if event.key == pygame.K_LEFT:
                dx = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP: dx = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT: dy = 0

    rect.move_ip(dx,dy)
    fondo.blit(canvas,rect)
    pygame.display.flip()