from collections import Counter


def find_anagrams(word, candidates):
    return [a for a in candidates if Counter(a.lower()) == Counter(word.lower()) and a.lower() != word.lower()]
