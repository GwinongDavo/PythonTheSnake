# Python Recursion
# What is recursion?
# Recursion is the process of defining something in terms of itself.
#
# Python Recursive Function
# In Python, we know that a function can call other functions.
# It is even possible for the function to call itself.
# These types of construct are termed as recursive functions.

# Following is an example of a recursive function to find the factorial of an integer.
#
# Factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
# Example of a recursive function
# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# num = 3
# print("The factorial of", num, "is", factorial(num))

# In the above example, factorial() is a recursive function as it calls itself.

# When we call this function with a positive integer,
# it will recursively call itself by decreasing the number.

# Each function multiplies the number with the factorial of the number below
# it until it is equal to one.

# Our recursion ends when the number reduces to 1. This is called the base condition.
#
# Every recursive function must have a base condition that stops the recursion
# or else the function calls itself infinitely.

# The Python interpreter limits the depths of recursion to help avoid infinite
# recursions, resulting in stack overflows.
# By default, the maximum depth of recursion is 1000.
# If the limit is crossed, it results in RecursionError.
# Let's look at one such condition.

def recursor():
    recursor()
recursor()

# Advantages of Recursion
# Recursive functions make the code look clean and elegant.
# A complex task can be broken down into simpler sub-problems using recursion.
# Sequence generation is easier with recursion than using some nested iteration.

# Disadvantages of Recursion
# Sometimes the logic behind recursion is hard to follow through.
# Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
# Recursive functions are hard to debug.
