

def rotate(text, key):
    """
    Returns the cipher text of a string for the corresponding key value.
    """
    lower = 'abcdefghijklmnopqrstuvwxyz'  # Our lower case string for reference
    upper = lower.upper()  # We make an upper case string as well
    secretkey = ''  # We'll store our answer in this variable

    cipherlower = lower[key:] + lower[:key]  # In these two lines we create the
    cipherupper = upper[key:] + upper[:key]  # lower and uppercase cipher texts.

    for char in text:

        if char in lower:
            secretkey += cipherlower[lower.index(char)]
        elif char in upper:
            secretkey += cipherupper[upper.index(char)]
        else:
            secretkey += char

    return secretkey
