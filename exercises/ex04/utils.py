"""List utility functions."""

__author__ = "730401590"


def all(numbers: list[int], value: int) -> bool:
    """This will see if the list are all the same numbers."""
    x: int = 1
    if x > len(numbers):
        return False
    i: int = 0
    while i < len(numbers):
        a: int = numbers[i]
        if a != value:
            return False
        i += 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """This will check if both lists are the same as each other."""
    if len(x) != len(y):
        return False
    i: int = 0
    while i < len(x):
        if x[i] != y[i]:
            return False
        i += 1
    return True 


def max(input: list[int]) -> int:
    """This will find the maximum number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    a: int = 1
    while i < len(input):
        if input[i] < input[a]:
            input.pop(i)
        else:
            return input[i]
    a += 1
    i += 1
    return input[i]