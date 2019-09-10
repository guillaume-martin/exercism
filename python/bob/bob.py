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

    # Remove meaningless trailing spaces
    hey_bob = hey_bob.rstrip()  
    # create a clean string that removes all non alphanumeric characters.
    clean_string = ''.join([char for char in list(hey_bob) if char.isalnum()])

    # is it a question?
    if len(hey_bob) > 0 and hey_bob[-1] == '?':
        response = "Calm down, I know what I'm doing!" if hey_bob.isupper() else 'Sure.'
    # if not, keep only alphanumeric characters and see what we have left
    elif len(clean_string) > 0:
        if clean_string.isupper():
            response = 'Whoa, chill out!'
        else:
            response = 'Whatever.'
    else:
        # The clean_string is empty which means we didn't say anything 
        response = 'Fine. Be that way!'

    return response
