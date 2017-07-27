from math import sqrt
from random import uniform, randint


class Orbit:
    semi_major_axis = 0
    eccentricity = 0
    inclination = 0

    semi_minor_axis = 0
    periapsis = 0
    apoapsis = 0

    period = 0
    velocity = 0
    motion = ''

    has_name = False
    name = ''

    def __init__(self, system, a, e, i, name):
        self.eccentricity = e
        self.inclination = i
        if name is not None:
            self.name = name
            self.has_name = True

        self.semi_minor_axis = a*sqrt(1-e**2)
        self.periapsis = a * (1 - e)
        self.apoapsis = a * (1 + e)
        self.velocity = sqrt(system.star_mass / a)

        if self.inclination in (0, 180):
            self.motion = 'equatorial'
        elif self.inclination == 90:
            self.motion = 'polar'

        if 0 <= self.inclination <= 90:
            self.motion += 'prograde'
        elif 90 < self.inclination <= 180:
            self.motion += 'retrograde'


class StandardOrbit(Orbit):
    def __init__(self, system, a, e=0, i=0, name=None):
        self.semi_major_axis = a
        self.period = sqrt((a ** 3) / system.star_mass)
        super().__init__(system, a, e, i, name)

    def __repr__(self):
        if self.name != '':
            return str(self.name)+' @'+str(round(self.semi_major_axis, 3))
        else:
            return str(round(self.semi_major_axis, 3))


class ResonantOrbit(Orbit):
    def __init__(self, system, gas_giant_orbital_p, resonance, e=0, i=0, name=None):
        x, y = [int(i) for i in resonance.split(':')]
        self.period = (y * gas_giant_orbital_p) / x
        self.semi_major_axis = a = ((self.period ** 2) * system.star_mass) ** (1 / 3)
        super().__init__(system, a, e, i, name)

    def __repr__(self):
        return 'Resonant Orbit'


class HotJupiterOrbit(StandardOrbit):
    def __init__(self, system, name):
        a = uniform(0.04, 0.5)
        e = uniform(0.001, 0.09)
        i = randint(-10, 10)
        if i < 0:
            i += 180
        super().__init__(system, a, e, i, name)
        if self.period < 3:
            raise ValueError('lower limit for orbital period exceeded')


class ClassicalGasGiantOrbit(StandardOrbit):
    def __init__(self, system, name=''):
        a = system.frost_line + uniform(1.0, 1.2)
        e = uniform(0.001, 0.09)
        i = randint(0, 90)
        super().__init__(system, a, e, i, name)


class SuperJupiterOrbit(StandardOrbit):
    def __init__(self, system, name=''):
        a = uniform(0.04, system.frost_line + uniform(1.0, 1.2))
        e = uniform(0.001, 0.09)
        i = randint(0, 90)
        super().__init__(system, a, e, i, name)


class GasDwarfOrbit(StandardOrbit):
    def __init__(self, system, name=''):
        a = uniform(system.frost_line + uniform(1.0, 1.2), system.outer_boundry)
        e = uniform(0.001, 0.09)
        i = randint(0, 90)
        super().__init__(system, a, e, i, name)


class TerrestialOrbit(StandardOrbit):
    def __init__(self, system, name=''):
        hi, ho = system.habitable_zone_inner, system.habitable_zone_outer
        a = uniform(hi, ho)
        e = uniform(0.0, 0.2)
        super().__init__(system, a, e, 0, name)
        if not self.periapsis >= hi or self.apoapsis <= ho:
            raise ValueError('terrestial orbit falls outside the habitable zone')
