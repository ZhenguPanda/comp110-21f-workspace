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

lines = ("Do not mistake temptation for opportunity.", "If you look back, you’ll soon be going that way.", "Flattery will go far tonight.")

str = results = random.choice(lines)

print("Your fortune cookie says...")
print(results)
print("Now, go spread positive vibes!")