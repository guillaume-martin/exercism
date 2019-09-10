def response(hey_bob):
    """ Returns Bob's response to what we say
    
    Parameters
    ----------
    hey_bob: String
        What is said to Bob
    
    Returns
    -------
    String
        Bob's response
    """

    hey_bob = hey_bob.rstrip()

    if hey_bob.endswith('?'):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.strip() == '':
        return "Fine. Be that way!"
    else:
        return "Whatever."
