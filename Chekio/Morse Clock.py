__author__ = 'v_shabalin'

# def checkio(time_string):
#     binary_count_minutes = ['....', '...-', '..-.', '..--', '.-..', '.-.-', '.--.', '.---', '-...', '-..-']
#     binary_count_hours = ['..', '.-', '-.']
#     result = ''
#     time_string = str(time_string).split(':')
#     for item in time_string:
#         if len(item) == 1:
#             item = '0' + item
#         result = result + ' ' + binary_count_hours[int(item[0])] + ' ' + binary_count_minutes[int(item[1])]
#         result = result + ' :'
#     return result[1:-2]

def checkio(time_string):

print checkio(u"10:37:49")