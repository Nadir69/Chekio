__author__ = 'v_shabalin'

def checkio(data):
     return len(data)>9 and\
            not data.isupper() and\
            not data.islower() and\
            not data.isalpha() and\
            not data.isdigit()


print checkio('aaaaASD1233123a')



