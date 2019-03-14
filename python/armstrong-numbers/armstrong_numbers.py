def is_armstrong(number):
    digits = list(str(number))
    length = len(digits)
    sum = 0
    for i in range(length):
        sum += int(digits[i])**length
    return True if sum == number else False
