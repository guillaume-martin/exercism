def gift_list(number):
    """Generates the list of gifts for a given verse

    Parameters
    ----------
    number: Integer
        The number of the verse we want the list for

    Returns
    -------
    string
        The list of gifts
    """
    gifts = {
        1: 'a Partridge in a Pear Tree',
        2: 'two Turtle Doves',
        3: 'three French Hens',
        4: 'four Calling Birds',
        5: 'five Gold Rings',
        6: 'six Geese-a-Laying',
        7: 'seven Swans-a-Swimming',
        8: 'eight Maids-a-Milking',
        9: 'nine Ladies Dancing',
        10: 'ten Lords-a-Leaping',
        11: 'eleven Pipers Piping',
        12: 'twelve Drummers Drumming'
    }

    return gifts[1] if number == 1 \
           else ', '.join([gifts[n] for n in reversed(range(2, number+1))]) + \
           f', and {gifts[1]}'

def recite(start_verse, end_verse):
    """ Generates a list of verses from the song Twelve days of Christmas

    Parameters
    ----------
    start_verse: Integer
        The number of the first verse to recite

    end_verse: Integer
        The number of the last verse to recite

    Returns
    -------
    list
        A list of verses from start_verse to end_verse
    """

    ordinals = {1:'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth', 6:'sixth',
                7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh',
                12:'twelfth'}

    return [f"On the {ordinals[num]} day of Christmas my true love gave to me: {gift_list(num)}."
            for num in range(start_verse, end_verse + 1) ]