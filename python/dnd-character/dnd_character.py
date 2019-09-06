import random

class Character:

    abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 
                 'wisdom', 'charisma']
    
    def __init__(self):
        for ability in self.abilities:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)


    def ability(self):
        dice = random.sample(range(1, 7), 4)
        dice.remove(min(dice))
        return sum(dice)


def modifier(constitution):
    return (constitution - 10) // 2
    
