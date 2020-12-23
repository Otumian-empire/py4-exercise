# exercise5.py
# function bersion of grade-score program

def computegrade(score):
    grade = ''

    try:
        score = float(score)

        if score < 0 or score >= 10:
            raise ValueError()
        elif score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        elif score < 0.6:
            grade = "F"

    except ValueError:
        grade = "Bad score"
    finally:
        return grade


print(computegrade(12.3))
print(computegrade('12.3'))
print(computegrade('2w12.3'))
