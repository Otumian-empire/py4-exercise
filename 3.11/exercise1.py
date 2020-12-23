# Exercise1.py

# Improved Exercise3.py - with conditions
# a program to prompt the user for hours and rate per
# hour to compute gross pay
#
# give the employee 1.5 times the hourly rate for hours
# worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

HOUR_LIMIT = 40
RATE_HOUR_LIMIT = 1.5

if hours > HOUR_LIMIT:
    bonus_hours = hours - HOUR_LIMIT
    bonus_rate = RATE_HOUR_LIMIT * rate
    bonus_pay = bonus_hours * bonus_rate

    pay = (rate * HOUR_LIMIT) + bonus_pay
else:
    pay = rate * hours

print(f"Pay: {pay:.2f}")
