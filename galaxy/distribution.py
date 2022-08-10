from math import pi, sin, cos, acos, floor
from decimal import Decimal
from random import choice


def stellar_neighbourhood(galactic_radius, location, radius, density, seed=1, home_preference=None):
    # galactic characteristc
    galactic_habitable_zone_inner = galactic_radius * 0.47
    galactic_habitable_zone_outer = galactic_radius * 0.6

    # stellar neighbourhood
    if home_preference is not None:
        warning = "This neighbourhood is uninhabitable"
        assert galactic_habitable_zone_inner <= location <= galactic_habitable_zone_outer, warning
    radius = Decimal(radius)
    stellar_density = round(Decimal(density), 3)

    _density = (stellar_density * (Decimal(4 / 3) * Decimal(pi) * Decimal(pow(radius, 3))))

    # Main sequence stars
    o = round(_density * Decimal(0.9) * Decimal(0.0000003))
    b = round(_density * Decimal(0.9) * Decimal(0.0013))
    a = round(_density * Decimal(0.9) * Decimal(0.006))
    f = round(_density * Decimal(0.9) * Decimal(0.03))
    g = round(_density * Decimal(0.9) * Decimal(0.076))
    k = round(_density * Decimal(0.9) * Decimal(0.121))
    m = round(_density * Decimal(0.9) * Decimal(0.7645))

    # White Dwarfs
    w = round(_density * Decimal(0.09))

    # Brown Dwarfs
    d = round(_density / Decimal(2.5))

    # Other Stellar Mass Objects
    other = floor(floor(_density * Decimal(0.01)))

    # Total Stellar Mass Objects in Stellar Neighbourhood
    total_mass = Decimal(round(sum([o, b, a, f, g, k, m, w, d, other])))
    stars = ['o']*o+['b']*b+['a']*a+['f']*f+['g']*g+['k']*k+['m']*m+['w']*w+['d']*d+['?']*other
    binary = round(((total_mass / Decimal(1.58)) * Decimal(0.33)))
    triple = round(((total_mass / Decimal(1.58)) * Decimal(0.08)))
    multiple = round(((total_mass / Decimal(1.58)) * Decimal(0.03)))
    single = round(total_mass - ((binary * 2) + (triple * 3) + (multiple * 4))) - 1
    total_systems = sum([single, binary, triple, multiple])

    seed = Decimal(seed)
    divisor = Decimal(2 ** 31 - 1)
    constante = Decimal(48271)
    initial_value = (constante * seed) % divisor
    r_raw = initial_value
    systems = {}
    if home_preference is not None:
        try:
            systems['Home'] = {"position": (0, 0, 0), 'composition': [stars.pop(stars.index(home_preference))]}
            delta = 1
        except ValueError:
            print(f'There are no {home_preference.capitalize()}-Stars in this Neighbourhood')
            return
    else:
        delta = 0

    for i in range(delta, total_systems + delta):
        if i <= single:
            prefix = 'Single'
            idx = i
            quantity = 1
        elif single < i <= single + binary:
            prefix = 'Binary'
            idx = i - (single + 1)
            quantity = 2
        elif binary < i <= single + binary + triple:
            prefix = 'Triple'
            idx = i - ((single + 1) + binary)
            quantity = 3
        else:
            idx = i - ((single + 1) + binary + triple)
            prefix = 'Multiple'
            quantity = 4

        p_raw = constante * r_raw % divisor
        q_raw = constante * p_raw % divisor
        r_raw = constante * q_raw % divisor

        p_normal = p_raw / divisor
        q_normal = q_raw / divisor
        r_normal = r_raw / divisor

        p = (p_normal ** Decimal(1 / 3)) * radius
        q = q_normal * Decimal(2) * Decimal(pi)
        r = acos(Decimal(2) * r_normal - Decimal(1))

        x = float(round(p * Decimal(sin(r)) * Decimal(cos(q)), 2))
        y = float(round(p * Decimal(sin(r)) * Decimal(sin(q)), 2))
        z = float(round(p * Decimal(cos(r)), 2))

        name = f"{prefix} Star System #{str(idx)}"

        composition = []
        for _ in range(quantity):
            if len(stars):
                star = choice(stars)
                stars.remove(star)
                composition.append(star)

        systems[name] = {'position': (x, y, z), 'distance': round(float(p), 2), 'composition': composition}
    return systems


sistemas = stellar_neighbourhood(5000, 2500, 10, 0.004, seed=14528, home_preference='g')
for sistema in sistemas:
    print(sistema, sistemas[sistema])

# as a general rule, the greater the distance between the center of the galaxy and the stellar neighbourhood, the
# less material (aka density) there is to form stars, so the two values should be merged into one variable.
# it is probably an exponential function.
