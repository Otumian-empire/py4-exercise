# exercise1.py
# a while loop that starts at the last character in the
# string and works its way backwards to the first character
# in the string, printing each letter on a separate line,
# except backwards.

sample_string = "The cat jumps over the moon"
str_size = len(sample_string)

while str_size >= 0:
    print(sample_string[str_size - 1])
    str_size -= 1
