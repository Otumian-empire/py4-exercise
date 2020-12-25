# exercise4.py
# a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the
# converted temperature

# Formula
# Fahrenheit = (Celsius x 1.8) + 32

deg_cel = float(input("Enter temperature in degree Celcius: "))
deg_fah = (deg_cel * 1.8) + 32

print(f"{deg_cel:.2f} = {deg_fah:.2f}")
