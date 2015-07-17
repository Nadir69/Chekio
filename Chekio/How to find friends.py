__author__ = 'v_shabalin'

def check_connection(network, first, second):
    newlist = []
    for item in network:
        newlist.append(item.split('-'))

    return newlist



print check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3")