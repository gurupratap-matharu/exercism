def is_leap_year(year):
    """Determine if a year is leap year or not."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
