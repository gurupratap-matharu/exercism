def detect_anagrams(word, candidates):
    lst = [x for x in candidates if x.lower() != word.lower()]
    word = ''.join(sorted(word.lower()))
    return [x for x in lst if word == ''.join(sorted(x.lower()))]
