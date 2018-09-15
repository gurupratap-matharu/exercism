
class Clock(object):
    def __init__(self, hour, minute):
        """
        The constructor function of the class.
        """
        total_minutes = (hour * 60) + minute
        hour, minute = divmod(total_minutes, 60)
        self.hour = hour % 24
        self.minute = minute

    def __repr__(self):
        """
        Returns the clock time as a string
        """
        return "{:02}:{:02}".format(self.hour, self.minute)

    def __eq__(self, other):
        """Checks if two clocks are equal. Returns a boolean value."""

        return (self.hour, self.minute) == (other.hour, other.minute)

    def __add__(self, minutes):
        """Add minutes to an existing clock."""
        hour = self.hour
        minute = self.minute + minutes

        return self.__class__(hour, minute)

    def __sub__(self, minutes):
        """Subtract minutes from an existing clock."""
        hour = self.hour
        minute = self.minute - minutes

        return self.__class__(hour, minute)
