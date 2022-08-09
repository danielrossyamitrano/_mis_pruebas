from math import pi, sin, cos, acos

radius = 10
seed = 1

initial_value = (48271 * seed) % (2 ** 31 - 1)

total = 17  # Total Star Systems in Stellar Neighbourhood
r_raw = initial_value
for i in range(1, total - 1):

    p_raw = 48271 * r_raw % 2 ** 31 - 1
    q_raw = 48271 * p_raw % 2 ** 31 - 1
    r_raw = 48271 * q_raw % 2 ** 31 - 1

    p_normal = p_raw / (2 ** 31 - 1)
    q_normal = q_raw / (2 ** 31 - 1)
    r_normal = r_raw / (2 ** (31 - 1))

    p = p_normal ** (1 / 3) * radius
    q = q_normal * 2 * pi
    r = acos(2 * r_normal - 1)

    x = round(p * sin(r) * cos(q), 2)
    y = round(p * sin(r) * sin(q), 2)
    z = round(p * cos(r), 2)

    print(x, y, z)
