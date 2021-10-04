"""Drawing forests in a loop."""

__author__ = "730401590"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

n: int = int(input("Depth: "))
s: str = ""
a = n


if n > 0:
    while n > 0:
        if a == n:
            s = TREE + s
        else:
            s = TREE + " " + s
        n = n - 1
    print(s)
else: 
    a = 0
