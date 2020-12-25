# exercise4.py
# functionn version of hour-rate program

def computepay(hours, rate):
    HOUR_LIMIT = 40
    RATE_HOUR_LIMIT = 1.5
    pay = 0

    try:
        hours = float(hours)
        rate = float(rate)

        if hours > HOUR_LIMIT:
            bonus_hours = hours - HOUR_LIMIT
            bonus_rate = RATE_HOUR_LIMIT * rate
            bonus_pay = bonus_hours * bonus_rate

            pay = (rate * HOUR_LIMIT) + bonus_pay
        else:
            pay = rate * hours

    except ValueError:
        print("Error, please enter numeric input")
    finally:
        return float(f"{pay:.2f}")
