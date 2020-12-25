# exercise2.py
# Improved Exercise3.py - with try and except
# using try and except so that your program handles
# non-numeric input gracefully by printing a message
# and exiting the program.

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

HOUR_LIMIT = 40
RATE_HOUR_LIMIT = 1.5

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hours > HOUR_LIMIT:
        bonus_hours = hours - HOUR_LIMIT
        bonus_rate = RATE_HOUR_LIMIT * rate
        bonus_pay = bonus_hours * bonus_rate

        pay = (rate * HOUR_LIMIT) + bonus_pay
    else:
        pay = rate * hours

    print(f"Pay: {pay:.2f}")

except ValueError:
    print("Error, please enter numeric input")
