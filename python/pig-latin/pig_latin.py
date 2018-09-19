def translate(text):
    """Converts string to piglatin."""

    text = text.split(' ')
    pig_latin = []

    # 1. We check if initial letter is a vowel
    for word in text:
        pig_latin.append(convert(word))

    return ' '.join(pig_latin)


def convert(word):
    # case 1
    if word[0].lower() in 'aeiou' or word[:2] == 'xr' or word[:2] == 'yt':
        return word + 'ay'

    else:

        if word[0] == 'y':
            return word[1:] + word[0] + 'ay'
        elif 'qu' in word:
            index = word.index('q')
            return word[index + 2:] + word[:index + 2] + 'ay'

        else:

            for count, letter in enumerate(word):
                if letter in 'aeiou' or letter == 'y':
                    return word[count:] + word[:count] + 'ay'
