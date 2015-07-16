__author__ = 'v_shabalin'

FIRST_TEN = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
SECOND_TEN = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
OTHER_TENS = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
HUNDRED = "hundred"

def checkio(number):
    snum = str(number)
    if number == 0:
        return ''
    if number < 10:
        return FIRST_TEN[number]
    elif number < 20:
        return SECOND_TEN[number-10]
    elif number < 100:
        return (OTHER_TENS[int(snum[0])] + ' ' + checkio(int(snum[1:]))).rstrip()
    else:
        return (FIRST_TEN[int(snum[0])] + ' hundred ' + checkio(int(snum[1:]))).rstrip()


print checkio(912)