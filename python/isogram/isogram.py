def is_isogram(string):
    string = string.replace(' ', '').replace('-', '').lower()
    return True if len(string) == len(set(string)) else False
