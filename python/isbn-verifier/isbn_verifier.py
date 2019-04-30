def verify(isbn):

    try:
        digits = list(isbn.replace('-', ''))

        # isbn has 10 digits
        assert len(digits) == 10

        # first 9 positions are numbers
        assert sum(int(d) in range(0, 10) for d in digits[:9]) == 9

        # replace X with 10
        if 'X' in digits:
            digits[digits.index('X')] = 10

        return True if  sum(int(d) * m for d, m in zip(digits, range(10, 0, -1)))%11 == 0 else False

    except:
        return False
