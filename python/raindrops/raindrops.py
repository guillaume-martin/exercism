def raindrops(number):
    factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    output = ''.join ([word for f, word in factors.items() if number % f == 0 ])
    return output if output else str(number)

