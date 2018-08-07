def is_pangram(sentence):
    """This function is the given string is a pangram or not. Returns a boolean value."""

    letters = 'abcdefghijklmnopqrstuvwxyz'  # our base string which all the 26 alphabets
    for letter in letters:
        # Now we check if each letter of our base string is in the passed argument
        if letter not in sentence.lower():
            return False
    return True


print(is_pangram("Five quacking Zephyrs jolt my wax bed."))
print(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."))
