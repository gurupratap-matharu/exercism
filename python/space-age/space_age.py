class SpaceAge(object):
    """Our SpaceAge class which calculates the age in earth years on different planets of our solar system. Returns floats upto 2 decimals.
    """

    def __init__(self, seconds):
        """Our main constructor class. We calculate the earth age here itself and
        use it in rest of the methods of our class"""
        self.seconds = seconds
        self.earthage = self.seconds / 31557600

    def on_mercury(self):
        return round(self.earthage / 0.2408467, 2)

    def on_venus(self):
        return round(self.earthage / 0.61519726, 2)

    def on_earth(self):
        return round(self.earthage, 2)

    def on_mars(self):
        return round(self.earthage / 1.8808158, 2)

    def on_jupiter(self):
        return round(self.earthage / 11.862615, 2)

    def on_saturn(self):
        return round(self.earthage / 29.447498, 2)

    def on_uranus(self):
        return round(self.earthage / 84.016846, 2)

    def on_neptune(self):
        return round(self.earthage / 164.79132, 2)

    def __str__(self):
        return "This class calculates the age of a person on various planets in 'earth-years' given the age of the person on earth in seconds."
