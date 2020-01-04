def count_words(phrase):
    """
    Returns a dict with count of each word in a phrase
    keys are the words and values the count of occurrence.
    """
    import re
    import string
    from collections import Counter
    phrase = phrase.lower()
    tokens = re.findall(r'[0-9a-zA-Z\']+', phrase)
    tokens = [word.strip(string.punctuation) for word in tokens]
    counts = Counter(tokens)
    return counts
