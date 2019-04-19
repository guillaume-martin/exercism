def raindrops(number):
    factors = {'3': 'Pling', '5': 'Plang', '7': 'Plong'}
    output = ''.join([factors[str(f)] for f in [3, 5, 7] if number % f == 0])
    return output if len(output) > 0 else str(number)

