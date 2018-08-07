def hey(phrase):
    """We shall check the phrase with certain built-in methods for parsing strings in the following order...
    1. Uppercase & question - for shouting and question.
    1. Uppercase - for shouting
    2. endswith '?' - for question
    3. empty string - for nothing
    4. all rest of the types will fall into another general category
    """
    phrase = phrase.strip()

    if phrase.isupper() and phrase.endswith('?'):
        return "Calm down, I know what I'm doing!"

    elif phrase.isupper():
        return "Whoa, chill out!"

    elif phrase.endswith('?'):
        return "Sure."

    elif phrase.strip() == '':
        return "Fine. Be that way!"

    else:
        return "Whatever."
