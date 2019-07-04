import re
def count_words(sentence):
    word_count = {}

    sentence = re.sub('[,_-]', ' ', sentence)

    words_list = [re.sub('[^A-Za-z0-9\']+', '', word.strip("'")) for word in sentence.lower().split()]

    for word in words_list:
        if len(word) > 0:
            try:
                word_count[word] += 1
            except KeyError:
                word_count[word] = 1

    return word_count

