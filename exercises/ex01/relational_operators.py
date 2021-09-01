"""Relational Operators: Allow the user to input two number variables and print out messages"""

__author__ = "730401590"

value_1 = str(input("Left-hand side: "))
value_2 = str(input("Right-hand side: "))

print(value_1, "<" + value_2, "is", bool(value_1 < value_2))
print(value_1, ">=", value_2, "is", bool(value_1 >= value_2)
print(value_1 + "==" + value_2, "is", bool(value_1 == value_2)
print (value_1, "!=", value_2, "is", bool(value_1 != value_2)