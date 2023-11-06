# def find(target, source):
#     for i in range(len(target)  -   len(source) +   1):
#         cnt=0
#         j=i
#         for index in range(len(source)):
#             if target[j] == source[index]:
#                 cnt +=  1
#         if cnt == len(source):
#             return i
#
#
#         return -1
#
#  print(find('string' , 'ing'))


# def find(target , source):
#     position = -1
#     j=0
#
#     for i in range(len(target)):
#         if target[i] != source[j]:
#             j=0
#             position = -1
#         if target[i]    ==  source[j]:
#             if j == 0:
#                 position = i
#         if j >= len(source) - 1:
#             break
#         else:
#             j+=1
#     return position
# print(find('string' , 'ing'))


# def check_sum(numbers , sum):
#     for number in numbers:
#         if sum - number in numbers:
#             return number , sum - number
#
#     return None
# print(check_sum([1,2,5,3] , 5))
# print(check_sum([1,2,5,3] , 9))

# def generate_multiple(num,length):
#     l=[]
#     i=1
#     while i <= length:
#         l.append(num*i)
#         i += 1
#
#     return l
#
# print(generate_multiple(3,4))


# ??
# def big_sum(a,b):
#     sum= ''
#     cf=0
#     i = len(a) - 1
#
#     while i >= 0:
#         s = int(a[i]) + int(b[i]) + cf
#         cf=0
#         if int(a[i]) + int(b[i]) > 9:
#             cf=1
#             s= str((int(a[i]) + int(b[i]))%10)
#         sum = s+sum
#         i -= 1
#     return sum
# print(big_sum("1214" , "212"))


def swap(word):
    vok='aeiou'
    voks=[]
    for ch in word:
        if ch in vok:
            voks.append(ch)
    s=''
    i=1
    for ch in word:
        if ch not in vok:
            s += ch
        else:
            s += voks [-i]
            i += 1

    return s



def test_swap(word):
    assert swap('terminator') == 'tormaniter'




def main():

    test_swap()
    main()





