"""Counting letters in a string."""

__author__ = "730401590"


letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))
i = len(word)
count = 0 

while i > 0:
    count = word.count(letter)
    i = i + 1
    break
print(len(letter))
