# exercise2.py
# a program that prompts for a list of numbers
# as above (exercise1.py) and at the end prints
# out both the maximum and minimum of
# the numbers instead of the average.


total = 0
count = 0
min_number = 1000
max_number = -1000

while True:
    number = input("Enter a number: ")

    if number == "done":
        print(f"total = {total}, count = {count}", end="")
        print(f", min = {min_number}, max = {max_number}")
        break

    try:
        number = int(number)
        total += number
        count += 1

        if number > max_number:
            max_number = number
        
        if number < min_number:
            min_number = number

    except ValueError:
        print("Invalid input")
