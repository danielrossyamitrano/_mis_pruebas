from pygame import init, quit, display, event, Surface
from pygame import KEYDOWN, QUIT, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, SRCALPHA, BLEND_RGBA_MIN, K_KP_PLUS, \
    K_KP_MINUS
from pygame.sprite import Sprite, LayeredUpdates
from sys import exit

init()

fondo = display.set_mode((600, 400))


class MyGroup(LayeredUpdates):
    def draw(self, surface):
        """draw all sprites in the right order onto the passed surface

        LayeredUpdates.draw(surface): return Rect_list

        """
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            if spr.tipo == 'Sombra':
                newrect = surface_blit(spr.image, spr.rect, special_flags=BLEND_RGBA_MIN)
            else:
                newrect = surface_blit(spr.image, spr.rect)
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty


group = MyGroup()

spra = Sprite()
spra.image = Surface((32, 32), SRCALPHA)
spra.image.fill((125, 125, 125, 125))
spra.tipo = 'Sombra'
spra.rect = spra.image.get_rect()

sprb = Sprite()
sprb.image = Surface((32, 32), SRCALPHA)
sprb.image.fill((125, 125, 125, 125))
sprb.tipo = 'Sombra'
sprb.rect = spra.image.get_rect(topleft=(50, 50))

char = Sprite()
char.image = Surface((32, 32), SRCALPHA)
char.image.fill((255, 0, 0, 255), (1, 1, 30, 30))
char.tipo = 'Mob'
char.rect = spra.image.get_rect(topleft=(150, 50))

group.add(spra, sprb, char)
layer = 0
while True:
    fondo.fill((0, 255, 125))
    events = event.get([KEYDOWN, QUIT, K_ESCAPE])
    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            quit()
            exit()
        elif e.type == KEYDOWN:
            if e.key == K_DOWN:
                spra.rect.y += 3
            if e.key == K_UP:
                spra.rect.y -= 3
            if e.key == K_LEFT:
                spra.rect.x -= 3
            if e.key == K_RIGHT:
                spra.rect.x += 3
            if e.key == K_KP_PLUS:
                layer += 1
                group.change_layer(spra, layer)
            if e.key == K_KP_MINUS:
                layer -= 1
                group.change_layer(spra, layer)

    group.draw(fondo)
    display.flip()
