import math
def kgv_math(a,b):
    return a * b // math.gcd(a, b)

def kgv_from_to(l, i_from, i_to):
    kgv = l[i_from]

    for i in range(i_from + 1, i_to + 1):
        kgv = kgv_math(kgv, l[i])

    return kgv
print(kgv_from_to([12,24,48,5,4,3,7,2,32,12,14,15,132], 0, 2))