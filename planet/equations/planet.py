from math import sqrt, pi
from random import uniform
from planet.constants import EARTH_RADIUS, EARTH_MASS, EARTH_GRAVITY
from planet.constants import EARTH_DENSITY, EARTH_ESCAPE_VELOCITY


class Planet:
    mass = 0
    radius = 0
    gravity = 0
    density = 0
    escape_velocity = 0
    composition = None

    def __init__(self, mass=None, radius=None, gravity=None):
        if not mass and not radius and not gravity:
            raise ValueError('must specify at least two values')

        if mass:
            self.mass = mass
        if radius:
            self.radius = radius
        if gravity:
            self.gravity = gravity

        if not self.gravity:
            self.gravity = mass / radius ** 2
        if not self.radius:
            self.radius = sqrt(mass / gravity)
        if not self.mass:
            self.mass = gravity * radius ** 2

        self.density = self.mass / self.radius ** 3
        self.escape_velocity = sqrt(self.mass / self.radius)
        self.composition = {}

    def absolutes(self):
        mass = self.mass * EARTH_MASS
        radius = self.radius * EARTH_RADIUS
        gravity = self.gravity * EARTH_GRAVITY
        velocity = self.escape_velocity * EARTH_ESCAPE_VELOCITY
        density = self.density * EARTH_DENSITY
        circumference = 2 * pi * radius
        surface_area = 4 * pi * (radius ** 2)
        volume = (4 / 3) * pi * (radius ** 3)
        return mass, radius, density, gravity, velocity, circumference, surface_area, volume


# Mass
# Dwarf planet: 0.0001 to 0.1 earth masses
# Terrestrial: 0.1 to 3.5 earth masses. use graph
# Gas Giant: 10 earth masses to 13 Jupiter masses
# PuffyGiant more than 2 Jupiter masses
# Gas Dwarf: 1 to 20 earth masses. use graph

# Radius:
# Dwarf planet: greater than 0.03 earth radius
# Earth sized: 0.5 to 1.5 earth radius
# Super earth:  1.25 to 2 earth radius
# Gas Giant:
# ------- if mass <= 2 Jupiter masses: less than 1 jupiter radius
# ------- elif 2 < mass <= 13 Jupiter masses: 1 +- 0.10 jupiter radius
# PuffyGiant: more than 1 jupiter radius
# Gas Dwarf less than 2 earth radius. use graph

# Gravity
# Terrestial: 0.4 to 1.6

class DwarfPlanet(Planet):
    def __init__(self):
        m = uniform(0.0001, 0.1)
        r = uniform(0.03, 0.5)
        super().__init__(mass=m, radius=r)


class TerrestialPlanet(Planet):
    def __init__(self):
        m = uniform(0.0001, 0.1)
        r = uniform(0.03, 0.5)
        super().__init__(mass=m, radius=r)


class GasGiant(Planet):
    def __init__(self):
        m = uniform(0.0001, 0.1)
        r = uniform(0.03, 0.5)
        super().__init__(mass=m, radius=r)
