#A drinking game version of Left-Center-Right
#Must have 3 players minimum, each player starts with 3 tokens/drinks
#Allow for self-drinking, a pot that the winner distributes among people
#1 game per Server
#People can drop mid-game, remaining drinks go to center
#Allow game ending in the middle in case of anything

import random

#Roll the dice and get either (s)tay, (c)enter, (l)eft, or (r)ight
def dice():
    return random.choice(['s', 's', 's', 'c', 'l', 'r'])

#def handler():
