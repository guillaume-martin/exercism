def verify(isbn):
    try:
        digits = list(isbn.replace('-', ''))

        # isbn has 10 digits
        assert len(digits) == 10

        # first 9 positions are numbers
        assert sum(int(d) in range(0, 10) for d in digits[:9]) == 9

        # the last position is either a number or an 'X'
        assert int(digits[9]) in range(0, 10) or digits[9] == 'X'

        return True if  sum(int(d) * m for d, m in zip(digits, range(11, 0, -1)))%11 == 0 else False
    
    except AssertionError:
        print('Not a valid ISBN')
        return False

    except ValueError:
        return False
