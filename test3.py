from itertools import filterfalse
def solution(A):
    b=len(A)
    jump=1
    if A[0]>b:
        return -1
    i = A[0]
    while i<=b:
        jump += 1
        i = i + A[i]
        print("i ",i, jump)
        if jump>b:
            return -1
        return jump

b=[1, 1, -1, 1]
A = [0, 3, -1, 1, 3]
print(solution(A))
# print(solution(b))








