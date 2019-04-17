def raindrops(number):
    factors = {
        '3':'Pling',
        '5':'Plang',
        '7':'Plong'
    }
    output = ''
    for factor in [3, 5, 7]:
        if number%factor == 0:
            output += factors[str(factor)]

    return output if len(output) > 0 else str(number)