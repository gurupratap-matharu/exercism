
class Clock(object):
    def __init__(self, hour, minute):
        """
        The constructor function of the class.
        """
        y, self.minute = divmod(minute, 60)
        hour += y
        x, self.hour = divmod(hour, 24)

    def __repr__(self):
        """
        Returns the clock time as a string
        """
        return "{:02}:{:02}".format(self.hour, self.minute)

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        """Add minutes to an existing clock."""
        added_minutes = self.minute + minutes
        __init__(self, self.hour, added_minutes)

        
    def __sub__(self, minutes):
        """Subtract minutes from an existing clock."""
        pass
#for i in range(0, 1000):
    #print(Clock(23, i))

