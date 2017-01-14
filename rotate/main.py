faces = ['front','right','back','left']
compass = ['north', 'east', 'south', 'west']

view = 'north'
face_A = 'front'
face_B = 'back'

n_view = 'south'
n_v_i = compass.index(n_view) #2

for n in [face_A,face_B]:
    idx = faces.index(n)
    j = [faces[idx]]+faces[idx+1:]+faces[:idx]
    new_face = j[n_v_i]
    
