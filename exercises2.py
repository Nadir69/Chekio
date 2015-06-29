__author__ = 'Merlo'


def buzz_words(number):
    if (number%3) == 0 AND (number%5)==0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return "Nothing is divisible by 3 or 5"

print buzz_words(6)
