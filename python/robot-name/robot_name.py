from string import ascii_uppercase
import random

def get_name():
    random.seed()
    name = ''
    for i in range(2):
        name += random_letter()
    for i in range(3):
        name += str(random_number())
    return name

def random_letter():
    return random.choice(ascii_uppercase)

def random_number():
    return random.randint(0,9)

class Robot(object):
    def __init__(self):
        self.name = get_name()

    def reset(self):
        self.name = get_name()
