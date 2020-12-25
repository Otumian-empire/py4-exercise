# exercise5.py
# a program the extracts the text after the colon
# then casts it to its type

string = 'X-DSPAM-Confidence:0.8475'

start = string.find(":")
if start > -1:
	print(string[start+1:])
else:
	print("There is no colon in string")
