"""Script that analyses the sentiment of a textual corpus"""

import string

WORD_MAP = {
    "good": 3,
    "better": 5,
    "amazing": 8,
    "superb": 9,
    "fantastic": 10,
    "wonderful": 9,
    "okay": 1,
    "bad": -5,
    "worse": -7,
    "disaster": -10,
    "horrible": -10,
    "reasonable": 2,
    "neutral": 0,
    "hate": -10,
    "love": 10,
}


def get_sentiment(text, word_map):
    """
    Identifies the overall sentiment of the text by taking the average
    of each word.

    Note: Words not found in the word_map dict are give zero value.
    """

    # remove all punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # split into tokens
    text = text.split()
    total_score, length = 0, 0

    # get score for each word, put zero if not found
    scores = (word_map.get(token.lower(), 0) for token in text)

    # find average score
    for score in scores:
        total_score += score
        length += 1

    return total_score / length


if __name__ == "__main__":
    text = "Amazing are clouds, SupERB are stars and wonderFUL the universe"
    print(f"{text} -> {get_sentiment(text, WORD_MAP)}")

    text = "I hate you!!!#@#"
    print(f"{text} -> {get_sentiment(text, WORD_MAP)}")

    text = "I love this ice cream. Its really amazing!!!!"
    print(f"{text} -> {get_sentiment(text, WORD_MAP)}")

    text = "Horrible disaster has struck us!!!!"
    print(f"{text} -> {get_sentiment(text, WORD_MAP)}")
