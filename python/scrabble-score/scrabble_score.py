
# First we store the scores for all the letters in a simple dictionary.
SCORES = {
    1: 'aeioulnrst',
    2: 'dg',
    3: 'bcmp',
    4: 'fhvwy',
    5: 'k',
    8: 'jx',
    10: 'qz',
}


def score(word):
    """
    Calculates the score of a scrabble word irrespective of the case.
    """
    total_score = 0

    for char in word:
        for key, values in SCORES.items():
            if char.lower() in values:
                total_score += key
                break
    return total_score
