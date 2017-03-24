from __future__ import division


class SpaceAge(object):
    EARTH_SECONDS = 31557600
    ORBITAL_PERIODS = {'earth': 1, 'mercury': .2408467,
                       'venus': .61519726, 'mars': 1.8808158,
                       'jupiter': 11.862615, 'saturn': 29.447498, 'uranus': 84.016846, 'neptune': 164.79132}

    def __init__(self, seconds):
        self.seconds = seconds


def planet_age_fn(planet):
    fn_name = 'on_' + planet

    def fn(self):
        return round(((self.seconds / SpaceAge.EARTH_SECONDS) * (1 / SpaceAge.ORBITAL_PERIODS[planet])), 2)
    setattr(SpaceAge, fn_name, fn)

for planet in SpaceAge.ORBITAL_PERIODS.keys():
    planet_age_fn(planet)
