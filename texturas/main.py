import pygame,sys,os
j = os.path.join

pygame.init()
ancho,alto = 640, 480
screen = pygame.display.set_mode([ancho, alto])
FPS = pygame.time.Clock()
fuente = pygame.font.SysFont('verdana',16,bold=True)

fondo1 = screen.copy()
fondo2 = screen.copy()

textura = pygame.image.load('pasto5.png')
for y in range(alto//32):
    y *= 32
    for x in range(ancho//32):
        x *= 32
        fondo1.blit(textura,(x,y))
render = fuente.render('Pasto5(noise)',True,(0,0,0))
fondo1.blit(render,(0,0))

textura = pygame.image.load('pasto3.png')
for y in range(alto//32):
    y *= 32
    for x in range(ancho//32):
        x *= 32
        fondo2.blit(textura,(x,y))
render = fuente.render('Pasto2(pencil)',True,(0,0,0))
fondo2.blit(render,(0,0))

fnd1 = True
while True:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                fnd1 = not fnd1
    if fnd1:
        screen.blit(fondo1,(0,0))
    else:
        screen.blit(fondo2,(0,0))
    pygame.display.flip()
