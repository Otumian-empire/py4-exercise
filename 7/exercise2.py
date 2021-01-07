# exercis2.py

# Exercise 2: Write a program to prompt for a file name,
# and then read through the file and look for lines of
# the form:

# X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

# Test your file on the mbox.txt and mbox-short.txt files.

STARTINGTEXT = "X-DSPAM-Confidence"

try:
    filename = input("Enter filename: ")
    # filename = "mbox-short.txt"
    sum_spam_conf = 0
    num = 0

    with open(filename, 'r') as fileobj:
        content = fileobj.readlines()

        for line in content:
            if line.startswith(STARTINGTEXT):
                sum_spam_conf += float(line.split(": ")[1])
                num += 1


    print(f"Average spam confidence:{sum_spam_conf/num}")
except Exception as e:
    print(e)
