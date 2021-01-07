# exercise3.py

# Sometimes when programmers get bored or want to have a
# bit of fun, they add a harmless Easter Egg to their program.
# Modify the program that prompts the user for the file name
# so that it prints a funny message when the user types in the
# exact file name “na na boo boo”. The program should behave
# normally for all other files which exist and don’t exist.
# Here is a sample execution of the program:

# sample input and output
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!


filename = input("Enter filename: ")

try:
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")

    else:
        with open(filename, 'r') as fileobj:
            size = len(fileobj.read())
            print(f"There were {size} subject lines in {filename}")

except FileNotFoundError:
    print(f"File cannot be opened: {filename}")
