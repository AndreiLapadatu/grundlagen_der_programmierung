# ex2
# def sum_diag(matrix):
#     result = []
#     for i in range(len(matrix)):
#         sum_linie = 0
#         for j in range(len(matrix[i])):
#             if i != j:
#                 sum_linie += matrix[i][j]
#
#         # if sum_linie == matrix[i][i]:
#         #     result.append(True)
#         # else:
#         #     result.append(False)
#         result.append(sum_linie == matrix[i][i])
#     return result
# def test_sum_diag():
#     assert sum_diag([
#         [4,3,1],
#         [1,2,1],
#         [0,5,1]
#         ]
#     ) == [True,True,False]
#
#     assert sum_diag([
#         [1,2,3],
#         [1,2,1],
#         [0,4,0]
#     ]) == [False,True,False]
#
def main():
#     test_sum_diag()
#     main()
#     test_max_line_file()
    test_count_palindrom()
#
# # ex4
#
# def max_line_file(filename):
#     f = open(filename, 'r')
#     result = []
#     for line in f:
#         max_lengh = 0
#         max_word = ''
#         words = line.split(' ')
#         for word in words:
#             word = word.strip()
#             if len(word) > max_lengh:
#                 max_word, max_lengh = word, len(word)
#         result.append(max_word)
#     f.close
#     return result
# def test_max_line_file():
#     assert max_line_file('data.input') == [4,4]

# def is_palindrom(word):
#     return word == word[::-1]
#
# def find_count(filename,word):
#     f = open(filename,'r')
#     count = 0
#
#     for linie in f:
#         words = line.split(' ')
#
#     for w in words:
#         if word == w.strip():
#             count += 1
#
#     f.close()
#     return count
#
# def count_palindrom(filename):
#     f = open(filename,'r')
#     result={}
#     for line in f:
#         words=line.split(' ')
#
#         for word in words:
#             if is_palindrom(word):
#                 result[word] = find_count(filename,word.strip())
#     f.close
#     return result
#
# def test_palindrom():
#     assert count_palindrom('data2.input') == {'anna':2,'abbcbba':1,'abba':2}

# ex1
# def nr_perfect(n):
#     sum=0
#     for d in range(1,n//2+1):
#         if n%d == 0:
#             sum+=d
#     if sum == n:
#         return True
#     else:
#         return False
#
# print(nr_perfect(28))

# def sum_coloana_perfect(matrix):
#     result = []
#     for i in range(len(matrix)):
#         sum_col = 0
#         for j in range(len(matrix)):
#             sum_col += matrix[j][i]
#         if(nr_perfect(sum_col) == True):
#             result.append(True)
#         else:
#             result.append(False)
#     for i in range(len(result)):
#         if result[i] == False:
#             return False
#     return True
#
# def test_sum_coloana():
#     sum_coloana_perfect([
#         [4,3,10],
#         [1,2,10],
#         [1,1,8]
#     ])  == [True]


# ex3
def kont_folge(a):

    for i in range(len(a)):
        for j in range(len(a[i])):
            if i%2 == 0:
                



