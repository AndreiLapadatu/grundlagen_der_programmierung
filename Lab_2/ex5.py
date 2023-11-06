
def filtru(l, ecuatie):
    new_l = []
    for i in l:
        x = i // 10
        y = i % 10
        if eval(ecuatie) == True:
            new_l.append(i)
    return new_l

print(filtru([84,42],'x/y==2'))
