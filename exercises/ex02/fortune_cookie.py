"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730401590"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
import random

a: str = "Do not mistake temptation for opportunity."
b: str = "If you look back, you’ll soon be going that way."
c: str = "Flattery will go far tonight."
d: str = "Be quiet for a little while."

e: int = random.randint(1, 4)

print("Your fortune cookie says...")
if e == 1: 
    print(a)
else:
    if e == 2:
        print(b)
    else:
        if e == 3:
            print(c)
        else:
            if e == 4:
                print(d)
print("Now, go spread positive vibes!")