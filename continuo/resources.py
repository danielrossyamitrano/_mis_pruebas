from pygame import image, Rect, mask
from pygame.sprite import DirtySprite

def cargar_imagen(ruta):
    return image.load(ruta).convert_alpha()

def split_spritesheet(ruta,w=32,h=32):
    spritesheet = cargar_imagen(ruta)
    ancho = spritesheet.get_width()
    alto = spritesheet.get_height()
    tamanio = w,h
    sprites = []
    for y in range(int(alto/h)):
        for x in range(int(ancho/w)):
            sprites.append(spritesheet.subsurface(Rect(((int(ancho/(ancho/w))*x,
                                                        int(alto/(alto/h))*y),
                                                        tamanio))))
    return sprites

class mob (DirtySprite):
    direcciones = {'abajo':[0,1],'izquierda':[-1,0],'arriba':[0,-1],'derecha':[+1,0],'ninguna':[0,0]}
    direccion = 'abajo'
    _step = 'S'
    
    def __init__(self,x,y):
        super().__init__()
        self.images = self.cargar_anims('heroe.png',['S','I','D'])
        self.image = self.images['S'+self.direccion]
        self.rect = self.image.get_rect(topleft = (x,y))
    
    def mover(self,dx,dy):
        
        self.animar_caminar()
        if dx > 0: self.direccion = 'derecha' 
        elif dx < -0: self.direccion = 'izquierda'
        
        if dy < 0: self.direccion = 'arriba'
        elif dy > 0: self.direccion ='abajo'
        
        self.rect.move_ip(dx,dy)
        
    @staticmethod
    def cargar_anims(ruta_imgs,seq,alpha=False):
        dicc = {}
        spritesheet = split_spritesheet(ruta_imgs)
        idx = -1
        for L in seq:
            for D in ['abajo','arriba','izquierda','derecha']:
                key = L+D
                idx += 1
                if not alpha:
                    dicc[key] = spritesheet[idx]
                else:
                    dicc[key] = mask.from_threshold(spritesheet[idx], C.COLOR_COLISION, (1,1,1,255))
        return dicc
    
    def animar_caminar(self):
        """cambia la orientación del sprite y controla parte de la animación"""

        if self.direccion != 'ninguna':
            if self._step == 'D':
                self._step = 'I'
            else:
                self._step = 'D'

            key = self._step+self.direccion

            self.image = self.images[key]