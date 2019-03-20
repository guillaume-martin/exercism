import string

def make_diamond(letter):
    letters = list(string.ascii_uppercase)
    index = letters.index(letter)
    diamond = []

    if index == 0:
        return 'A\n'
    
    row_length = 2 * index + 1
    # upper half
    for row in range(index + 1):
        outer_spaces = index - row 
        inner_spaces = row_length - (outer_spaces * 2) - 2
        row_str = ' ' * outer_spaces + letters[row] 
        if row > 0:
            row_str += ' ' * (inner_spaces) + letters[row]
        row_str += ' ' * outer_spaces
        diamond.append(row_str)
        

    # lower half
    for row in diamond[index-1::-1]:
        diamond.append(row)
        
    return '\n'.join(diamond) + '\n'

