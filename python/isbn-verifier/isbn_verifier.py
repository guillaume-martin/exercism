import re

def verify(isbn):

    regex = '[0-9]{9}([0-9]|X)'

    try:
        # control format
        isbn = isbn.replace('-', '')
        re.match(regex, isbn)

        # replace X with 10
        isbn = isbn.replace('X', '')

        return True if  sum(int(d) * m for d, m in zip(list(isbn), range(10, 0, -1)))%11 == 0 else False

    except:
        return False
