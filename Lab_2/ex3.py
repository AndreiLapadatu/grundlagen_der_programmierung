def sort(l):
    i=0
    for k in range (i , len(l)):
        for j in range (i+1 , len(l)):
            if(l[k] < l[j]):
                l[k], l[j] = l[j], l[k]
        i += 1
    return l



print(sort([4,5,76,77,4,3,3,2,55,7]))

l=sort([4,5,76,77,4,3,3,2,55,7])
b = [str(l) for l in l]
print(''.join(b))

