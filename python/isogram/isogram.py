def is_isogram(string):
    """Checks whether a given string is isogram or not. Returns a boolean."""

    string = string.lower()

    lst = [char for char in list(string) if char in 'abcdefghijklmnopqrstuvwxyz']
    for char in lst:
        if lst.count(char) > 1:
            return False
    return True
