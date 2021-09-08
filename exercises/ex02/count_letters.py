"""Counting letters in a string."""

__author__ = "730401590"


letter: str = str(input("What letter do you want to serach for?: "))
word: str = str(input("Enter a word: "))
i = 0

while i < len(word):
    i = i + 1
print("Count:", int(i - 1))