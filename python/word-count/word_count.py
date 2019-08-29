import re
from collections import Counter

def count_words(sentence):
    word_count = {}

    sentence = re.sub('[,_-]', ' ', sentence)

    words_list = [w for w in [re.sub('[^A-Za-z0-9\']+', '', word.strip("'")) for word in sentence.lower().split()] if len(w) > 0]
    counter = Counter(words_list)

    return counter

