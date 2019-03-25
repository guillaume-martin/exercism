def distance(strand_a, strand_b):
    try:        
        assert len(strand_a) == len(strand_b)
        
        return len([b for a, b in zip(strand_a, strand_b) if b != a])

    except AssertionError:
        raise ValueError('The two strands are of different length.')