# exercise1.py
# Exercise 1: Write a function called chop
# that takes a list and modifies it, removing
# the first and last elements, and returns None.
# Then write a function called middle that takes
# a list and returns a new list that
# contains all but the first and last elements.


def chop(param: list):
	param.pop(0)
	param.pop()

	return None


def middle(param: list):
	new_param = param
	chop(new_param)

	return new_param

