def distance(strand_a, strand_b):
    try:
        str_lght = len(strand_a)
        assert len(strand_b) == str_lght
        
        distance = 0
        for idx in range(str_lght):
            if strand_a[idx] != strand_b[idx]:
                distance += 1
        
        return distance

    except AssertionError:
        raise ValueError('The two strands are of different length.')