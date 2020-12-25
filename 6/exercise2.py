# exercise2.py

'''
word = 'banana'
count = 0
for letter in word:
	if letter == 'a':
		count = count + 1
print(count)
'''

# an encapsulation the above code into a function named count,
# and generalizing it so that it accepts the string and the
# letter as arguments.


def count(word, letter):
    count = 0

    for ch in word:
        if ch == letter:
            count += 1

    return count

