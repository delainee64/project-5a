# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/24/2022
# Description: Write a recursive function named multiply
# that takes two positive integers as parameters and returns the product of those two numbers.

def multiply(pos_1, pos_2):
    """Function finds the product of two positive numbers without using multiplication."""
    if pos_2 >= 1:
        return pos_1 + multiply(pos_1, pos_2 - 1)
    else:
        return 0

# print(multiply(8, 4))
# print(multiply(54, 8))
# print(multiply(10, 0))
