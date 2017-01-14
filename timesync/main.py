from pygame import time
from datetime import datetime

fps = time.Clock()
second_real = datetime.now().time().second
second_fictional = 0

shows = ['fiction','real']
show  = 1

while True:
    fps.tick(60)
    
    mom = datetime.now().time()
    h = mom.hour
    m = mom.minute
    tick = mom.second
    
    if second_real != tick:
        second_real = tick
        second_fictional += 1
        
    if shows[show] == 'fiction':
        print(second_fictional)
    elif shows[show] == 'real':
        print(h,':',m,sep='')
