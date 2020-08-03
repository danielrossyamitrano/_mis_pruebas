import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# we create two "shadow" surfaces, a.k.a. black with alpha channel set to something
# we use these to illustrate the problem
shadow = pygame.Surface((128, 128), pygame.SRCALPHA)
shadow.fill((0, 0, 0, 100))
shadow2 = shadow.copy()

# a helper surface we use later for the fixed shadows
shadow_surf = pygame.Surface((800, 600))
# we set a colorkey to easily make this surface transparent
colorkey_color = (2, 3, 4)
shadow_surf.set_colorkey(colorkey_color)
# the alpha value of our shadow
shadow_surf.set_alpha(100)

# just something to see the shadow effect
test_surface = pygame.Surface((800, 100))
test_surface.fill(pygame.Color('cyan'))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color('white'))

    screen.blit(test_surface, (0, 150))

    # first we blit the alpha channel shadows directly to the screen 
    screen.blit(shadow, (100, 100))
    screen.blit(shadow2, (164, 164))

    # here we draw the shadows to the helper surface first
    # since the helper surface has no per-pixel alpha, the shadows
    # will be fully black, but the alpha value for the full Surface image
    # is set to 100, so we still have transparent shadows
    shadow_surf.fill(colorkey_color)
    shadow_surf.blit(shadow, (500, 100))
    shadow_surf.blit(shadow2, (564, 164))

    screen.blit(shadow_surf, (0, 0))

    pygame.display.update()
