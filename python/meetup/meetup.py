from datetime import date


def meetup_day(year, month, day_of_the_week, which):
    """
    Based on the query returns the meetup day of a month as a date object.
    """

    codes = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7,
        '1st': 0,
        '2nd': 1,
        '3rd': 2,
        '4th': 3,
        '5th': 4,
        'last': -1,

    }

    if which == 'teenth':

        for day in range(13, 20):  # Since 13-19 are the 'teenth' dates in a month.
            d = date(year, month, day)

            if d.isoweekday() == codes[day_of_the_week]:
                return d

    elif which in ['1st', '2nd', '3rd', '4th', '5th', 'last']:
        possible_meetups = []  # We'll store all possible meetup dates here.

        for day in range(1, 32):
            try:
                d = date(year, month, day)

            except ValueError:
                pass

            finally:
                if d.isoweekday() == codes[day_of_the_week]:
                    possible_meetups.append(d)

        return possible_meetups[codes[which]]


def MeetupdayException():
    raise ValueError('Day does not exist.')
