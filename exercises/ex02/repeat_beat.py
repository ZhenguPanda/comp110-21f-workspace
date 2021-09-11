"""Repeating a beat in a loop."""

__author__ = "730401590"


word: str = (input("What beat do you want to repeat? "))
n: int = int(input("How many times do you want to repeat it? "))
s: str = ""
a = n

if n > 0:
    while n > 0:
        if a == n:
            s = word + s
        else:
            s = word + " " + s
        n = n - 1
    print(s)
else: 
    print("No beat...")