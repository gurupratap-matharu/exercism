import datetime


def add_gigasecond(birth_date):
    """
    Returns the moment when someone has lived for 10^9 seconds!
    Did you know?
    10^9 seconds = 11574 days and 6400 seconds.
    """

    delta = datetime.timedelta(seconds=10**9)
    return birth_date + delta
