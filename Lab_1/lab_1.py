# # # Lab_1
# # # ex5_ex9

# #     # 5.a.
#
# def exponenten(n, p):
#      exp = 0
#      while n > 1:
#         if n%p == 0:
#             exp += 1
#             n //= p
#         else:
#              break
#      return exp
# print(exponenten(18,3))
#
# ------------------------------

# 5.b.
# def ist_relativ_prim(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a==1
#
# def langste_teilfolge(zahlen):
#     n = len(zahlen)
#     max_len = 0
#     aktuell_len = 0
#     start_idx = 0
#     max_idx = 0
#
#     for i in range(1, n):
#         if ist_relativ_prim(zahlen[i - 1], zahlen[i]):
#             aktuell_len += 1
#             if aktuell_len > max_len:
#                 max_len = aktuell_len
#                 max_idx = start_idx
#         else:
#             aktuell_len = 0
#             start_idx = i
#     print(max_idx)
#     return zahlen[max_idx:max_idx+max_len+1]
# print(langste_teilfolge([8,21,103,27,9,44]))

# -------------------------------------------------------

# # 9.a.
# #
# def primfaktorenzerlegung(n):
#     l = []
#     d=2
#     while   n != 1  :
#         if n % d == 0:
#             l.append(d)
#             n //= d
#         else:
#             d += 1
#
#     return l
# print(primfaktorenzerlegung(24))
# #
# #   --------------------------------------------------
# #
# # # 9.b.
# #
# def längste_Teilfolge(zahlenvek):
#
#     if not zahlenvek:
#         return []
#
#     i=0
#     n=zahlenvek[i]















 print(längste_Teilfolge([777777,7777,77,77,7,8,8,1]))
# #
#
#
#
#
