def verschlusseln(l):
    new_l = []
    x = l[0]

    for i in range(len(l)):
        new_l.append(l[i] + x)

    return new_l
print (verschlusseln([12,4,5,6]))


def verschlusseln(l):
    new_l = []
    x = l[0]

    for i in range(len(l)):
        new_l.append(l[i] * x)

    return new_l
print (verschlusseln([12,4,5,6]))

def verschlusseln(l):
    new_l = []
    x = l[0]

    for i in range(len(l)):
        new_l.append(l[i] ^ x)

    return new_l
print (verschlusseln([12,4,5,6]))
