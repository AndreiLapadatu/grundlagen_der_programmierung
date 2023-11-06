def descomp(x):
    while x > 10:
        x //= 10
    return x

def uc(y):
    x = y % 10
    return x


def maxdomino(domino):
    l= []
    ct = 0
    max = 0
    i = 0
    while i < (len(domino) - 1):
        aux = domino[i]
        aux2 = domino[i + 1]
        if uc(aux) == descomp(aux2):
                 ct += 1
                 l.append(domino[i])
                 l.append(domino[i+1])
        i += 2
        if max < ct:
            max=ct
            ct=0

    return l

print(maxdomino([5,4,76,63,21,13,35,56]))




