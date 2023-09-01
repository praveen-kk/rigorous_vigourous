"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
# def sol(A):
#     b=sorted(A)
#     print(b)
#     l=len(b)
#     if b[l-1]<0:
#         return 1
#
#     c=[]
#     for i in range(0,l):
#
#         if (b[i]>0):
#             c.append(b[i])
#
#             if (b[i]-1)>0:
#                 return b[i]-1
#                 break
#             elif(b[i]+1) not in b:
#                 return b[i]+1
#             i+=1
#         else:
#
#
#
#
#
#         i+=1
#
#         # else:
#         #     return 1

from itertools import count, filterfalse
def minpositive(a):
    return next(filterfalse(set(a).__contains__, count(1)))

    # return (next(filterfalse(set(a).__contains__, count(1))))





    # for i in b:
    #     if
A=[-1, 4, 4, 1, 6, 8, 8, 8 , 8, 5, 5, 8 , 7, 9, 10, 18, 11, 13, 14, 12, 8]
print(minpositive(A))
