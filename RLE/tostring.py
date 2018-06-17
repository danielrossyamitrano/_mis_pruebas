from pygame import init, Surface, image
init()
img = Surface((10,10))
img.fill((255,0,255),(3,7,4,3))

st = str(image.tostring(img,'RGB'))
print(st)
