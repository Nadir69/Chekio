__author__ = 'v_shabalin'


def find_message(text):
    response = ""
    for letter in text:
        if letter.isupper():
            response += letter
    return response

print find_message("How are you? Eh, ok. Low or Lower? Ohhh.")