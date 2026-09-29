#funtions2.py
#functions with return and without parameters
from random import randint
import os

def rollDice():
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return die1, die2

#main
dice = rollDice()
print(f"Dice: {dice}")
if dice[0] == 6 and dice[1] == 6:
    print ("you win!!")
else:
    print ("Try again!!")