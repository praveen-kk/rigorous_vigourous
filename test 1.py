# import math
#
#
# def solution(X, Y, D):
#
#     # write your code in Python 3.6
#
#     num = Y - X
#     den = D
#     # jumps = math.ceil(num / den)
#     jumps = num%D
#
#     return jumps
#
# print(solution(85,10, 30/)
# A[p] + A[Q] =K
from itertools import filterfalse

def solution(K,A):
    l=len(A)
    complimentary_pair=0
    for p in range(l):
        for q in range(l):
            if (A[p] +A[q]==K):
                complimentary_pair += 1
    return complimentary_pair

A=[1, 8, -3, 0, 1, 3, -2, 4, 5]
K=6
print(solution(K,A))


