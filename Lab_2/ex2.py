def inv(nr):
    x=0
    p=1
    while nr:
        x = x * p + nr % 10
        p *= 10
        nr //= 10
    return x

def symmetrisch(n):
    ct=0
    i=0
    while i <= len(n):
        for j in range(i + 1, len(n)):
            if n[i] == inv(n[j]):
                ct += 1
        i += 1
    return ct

print (symmetrisch([76,7,33,33,4,5,6,32,23,15,23]))


