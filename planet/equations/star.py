from planet.constants import SOL_MASS, SOL_LUMINOSITY, SOL_RADIUS, SOL_TEMPERATURE, SOL_LIFETIME, STELAR_CLASIFICATION
from math import pi


class Star:
    mass = 1
    radius = 1
    luminosity = 1
    temperature = 1
    lifetime = 1
    tipo = 'G'

    def __init__(self, m):
        self.mass = m
        if self.mass < 1:
            self.radius = self.mass ** 0.8
        elif self.mass > 1:
            self.radius = self.mass ** 0.5
        self.luminosity = m ** 3.5
        self.lifetime = m / self.luminosity
        self.temperature = (self.luminosity / (self.radius ** 2)) ** (1 / 4)

        for key in STELAR_CLASIFICATION:
            minimo, maximo = STELAR_CLASIFICATION[key]
            if minimo <= self.mass <= maximo:
                self.tipo = key
                break

    def absolutes(self):
        mass = self.mass * SOL_MASS
        radius = self.radius * SOL_RADIUS
        luminosity = self.luminosity*SOL_LUMINOSITY
        temperature = self.temperature*SOL_TEMPERATURE
        lifetime = self.lifetime*SOL_LIFETIME
        circumference = 2 * pi * radius
        surface_area = 4 * pi * (radius ** 2)
        volume = (4 / 3) * pi * (radius ** 3)
        return mass, radius, luminosity, temperature, lifetime, circumference, surface_area, volume

    def __repr__(self):
        return 'Star'
