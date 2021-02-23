from math import cos, pi

def axial_precession(year):
    a1 = 19.87 # minimum axial tilt value
    a2 = 20.21 # maximum axial tilt value
    m = 34000 # period of the precession
    
    # from: https://www.youtube.com/watch?v=a5aAIbTs_Gw
    b = (a1 + a2)/2
    a = a2-b
    y = a*cos((2*pi/m)*year-pi)+b
    return y