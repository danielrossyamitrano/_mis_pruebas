from pygame import display, event, QUIT, KEYDOWN, KEYUP, K_ESCAPE, init, quit, Surface, K_UP, K_DOWN, draw, font, K_SPACE, time
from math import sin, cos, pi, sqrt,radians
from sys import exit

init()
fondo = display.set_mode((400,400))
rect_fondo = fondo.get_rect()
fps = time.Clock()

fuente1 = font.SysFont('Verdana',16)
fuente2 = font.SysFont('Verdana',14)

negro = (0,0,0)
blanco =(255,255,255)

render_x = fuente1.render('x',1,negro)
render_y = fuente1.render('y',1,negro)
render_z = fuente1.render('z',1,negro)

rect_x = render_x.get_rect(x=rect_fondo.right-10,y=rect_fondo.centerx)
rect_top = render_y.get_rect(x=rect_fondo.centerx+2,y=0)
rect_mid = render_z.get_rect(x=rect_fondo.centerx-10,y=rect_fondo.centery)

text_a = 'Adjusting the Argument of periapsis'.center(45,' ')
text_b = 'Adjusting the Longitude of the ascending node'

render_text_a = fuente2.render(text_a,1,negro)
render_text_b = fuente2.render(text_b,1,negro)

rect_text=render_text_b.get_rect(centerx=rect_fondo.centerx,bottom=rect_fondo.bottom)

render_rotation = fuente2.render('Rotation: ',1,negro)
rect_rotation = render_rotation.get_rect()

a = 1
e = 0.7
b = (sqrt(1-pow(e,2)))
c = sqrt(pow(a,2)-pow(b,2))

delta = 100
a*=delta
b*=delta
c*=delta

c1,c2 = 200, 200
offset_x = c1
offset_y = c2
rotation = 270
def draw_ellipse(rot_angle, size):
    img = Surface(size)
    img.fill(blanco)
    rect = img.get_rect()
    
    draw.line(img,negro,rect.midleft,rect.midright,1)
    draw.line(img,negro,rect.midtop,rect.midbottom,1)
    colors = [(255,0,0), (0,255,0), (0,0,255)]
    for angle in range(1, 361):
        if angle <= 120:
            color = colors[0]
        elif 120 < angle <= 240:
            color = colors[1]
        else:
            color = colors[2]

        ang = radians(angle)
        r = radians(rot_angle)
        cos_r, sin_r = cos(r), sin(r)
        cos_a, sin_a = cos(ang), sin(ang)
        
        x1 = c * cos_r
        y1 = c * sin_r
        
        x = offset_x + x1 + a * cos_a * cos_r - b * sin_a * sin_r
        y = offset_y + y1 + b * sin_a * cos_r + a * cos_a * sin_r 
        img.set_at((int(x),int(y)),color)
    
    draw.circle(img,negro,(c1, c2),3)
    draw.circle(img,(0,255,255),(x1+c1, y1+c2),3)
    draw.circle(img,(255,0,255),(c2+2*x1, c2+2*y1),3)
    
    return img

rect_a = rect_top
rect_b = rect_mid

dr = 0
img = draw_ellipse(rotation,rect_fondo.size)
do_draw = True
text = render_text_b
while True:
    fps.tick(60)
    events = event.get([QUIT, KEYDOWN, KEYUP])
    event.clear()
    for e in events:
        if (e.type == QUIT) or (e.type==KEYDOWN and e.key==K_ESCAPE):
            quit()
            exit()
        elif e.type==KEYDOWN:
            if e.key == K_UP:
                dr = -1
                do_draw = True
            elif e.key == K_DOWN:
                dr = +1
                do_draw = True
            elif e.key == K_SPACE:
                if rect_a == rect_top:
                    rect_a = rect_mid
                    rect_b = rect_top
                    text = render_text_a
                else:
                    rect_a = rect_top
                    rect_b = rect_mid
                    text = render_text_b
                rotation = 270
                do_draw = True
             
        elif e.type == KEYUP:
            dr = 0
            do_draw = False
    
    if -90 <= rotation + dr <= 270:
        rotation += dr
        actual_rotation = round(abs(rotation-270),3)
          
    if do_draw == True:
        img = draw_ellipse(rotation,rect_fondo.size)
    
    fondo.blit(img,(0,0))
    fondo.blit(render_x, rect_x)
    fondo.blit(render_y, rect_a)
    fondo.blit(render_z, rect_b)
    
    fondo.fill(blanco,rect_text)
    fondo.blit(text,rect_text)
    
    fondo.blit(render_rotation, rect_rotation)
    fondo.blit(fuente2.render(str(actual_rotation)+'°',1,negro),rect_rotation.topright)
    display.update()