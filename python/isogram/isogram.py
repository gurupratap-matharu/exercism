def is_isogram(string):
    """Checks whether a given string is isogram or not. Returns a boolean."""

    string = string.lower().replace(' ', '').replace('-', '')

    return len(string) == len(set(string))
