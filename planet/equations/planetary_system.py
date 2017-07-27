from math import sqrt
from random import uniform
from planet.equations.orbit import StandardOrbit
from planet.equations.orbit import ClassicalGasGiantOrbit, TerrestialOrbit


class PlanetarySystem:
    stable_orbits = []
    inner_boundry = 0
    outer_boundry = 0

    def __init__(self, star_mass, star_luminosity, habitable=True):
        self.star_mass = star_mass
        self.star_luminosity = star_luminosity

        self.inner_boundry = star_mass * 0.01
        self.outer_boundry = star_mass * 40

        self.frost_line = 4.85 * sqrt(star_luminosity)
        self.habitable_zone_inner = sqrt(star_luminosity / 1.1)
        self.habitable_zone_outer = sqrt(star_luminosity / 0.53)

        self.stable_orbits = [ClassicalGasGiantOrbit(self, name='largest_gas_giant_orbit')]
        if habitable:
            self.stable_orbits.append(TerrestialOrbit(self, name='habitable_orbit'))

        self.add_orbits('distant')
        self.add_orbits('closing')
        self.check_orbits()

    def add_orbits(self, method):
        orbit = self.stable_orbits[0].semi_major_axis
        while True:
            variance = uniform(1.4, 2.0)
            if method == 'closing':
                orbit /= variance
            elif method == 'distant':
                orbit *= variance

            if self.inner_boundry < orbit < self.outer_boundry:
                self.stable_orbits.append(StandardOrbit(self, orbit))
            else:
                break

    def check_orbits(self):
        self.stable_orbits.sort(key=lambda orbit: orbit.semi_major_axis)
        orbits = self.stable_orbits
        delete = []
        lenght = len(self.stable_orbits)
        for i in range(len(self.stable_orbits)):
            if not orbits[i].has_name and i + 1 < lenght:
                if orbits[i].semi_major_axis + 0.15 > orbits[i + 1].semi_major_axis:
                    delete.append(orbits[i])

        for flagged in delete:
            if flagged in self.stable_orbits:
                self.stable_orbits.remove(flagged)


class SolarSystem(PlanetarySystem):
    def __init__(self, star, habitable=True):
        super().__init__(star.mass, star.luminosity, habitable)

    def __repr__(self):
        return 'Solar Star System'


class PTypeSystem(PlanetarySystem):
    def __init__(self, primary, secondary, avgsep, habitable=True):

        if primary.mass <= secondary.mass:
            self.primary = primary
            self.secondary = secondary
        else:
            raise ValueError()

        if 0.15 < avgsep < 6:
            raise ValueError('Average Separation too pronounced')
        else:
            self.average_separation = avgsep

        combined_mass = primary.mass + secondary.mass
        combined_luminosity = primary.luminosity + secondary.luminosity
        super().__init__(combined_mass, combined_luminosity, habitable)

    def __repr__(self):
        return 'P-Type Star System'
