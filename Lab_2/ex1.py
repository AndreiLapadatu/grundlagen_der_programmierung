def entfernen(repeat):
    l = []
    for i in range(len(repeat)):
        if repeat[i] not in l:
            l.append(repeat[i])
    return l

print(entfernen([1,2,3,4,5,6,6,6,7]))

