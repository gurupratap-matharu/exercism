import re


def abbreviate(words):
    """Returns an acronym for the words passed."""

    words = words.upper()

    # We split the string with delimiters of <space> or <hyphen>
    sentence = re.split(' |-', words)
    acronym = ''

    for word in sentence:
        acronym += word[0]
    return acronym
