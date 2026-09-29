from random import randint
import os

i = 1
while i <= 10:
    key = input("Press any key to roll the dice :::")
    print(f"::: Roll {i} :::")
    print(f"Dice 1: {randint(1, 6)}")
    print(f"Dice 2: {randint(1, 6)}")
    print("/n")
    i += 1
rollDice()
