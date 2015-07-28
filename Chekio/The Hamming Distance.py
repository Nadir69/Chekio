__author__ = 'v_shabalin'

def checkio(n, m):
    n = [x for x in bin(n)]
    m = [x for x in bin(m)]
    diff = abs(len(n) - len(m))
    result = 0
    while diff > 0:
        if len(n)>len(m):
            m.insert(2,'0')
            diff -= 1
        else:
            n.insert(2,'0')
            diff -= 1
    for item in range(len(n)):
        if n[item] != m[item]:
            result += 1
    return result

print checkio(16, 15)