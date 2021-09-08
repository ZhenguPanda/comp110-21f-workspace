"""Repeating a beat in a loop."""

__author__ = "730401590"


word: str = (input("What beat do you want to repeat? "))
n: int = int(input("How many times do you want to repeat it? "))
s: str = " "

while n > 0:
    s = word + " " + s 
    n = n - 1
if n < 0: 
    print("No beat...")
print(s)