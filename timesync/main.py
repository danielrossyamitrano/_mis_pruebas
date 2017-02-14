from pygame import time
from .clock import Clock

fps = time.Clock()
clock = Clock(h=7, m=51, real=False)

_frames = 0
rate = 60

clock.enabled = True
dia = 0

while True:  # esto representa Tiempo.update()
    fps.tick(rate)

    _frames += 1
    if _frames == rate:
        clock.update()
        _frames = 0

        if clock.day_flag:
            dia += 1
        if clock.hour_flag:
            print(clock.timestamp())
        if clock.minute_flag:
            print(clock.timestamp())
