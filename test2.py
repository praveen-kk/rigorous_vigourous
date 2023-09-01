# def solution(N):
#     F(0)=0
#     F(1)=1
#     F(N)=F(N-1)+F(N-2) if N>=2
#     return lambda N:(N-1)+

# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#       return 0
#     else:
#       return fib(n-1) + fib(n-2)
# print(fib(36))
import math
def solution(N):
    a=pow(2 << N, N + 1, (4 << 2*N) - (2 << N) - 1) % (2 << N)
    b=str(a)
    l=len(b)
    if l>=6:
        return int(b[-6:])
    return int(f"{a:06}")
    # return a
    # l=len(a)
    # print(l)
    # if l>6:
    #     return a[l:l-6]
print (solution(350))
###############################################################################################

# print(fib(55))


# Python code to find last two
# digits of n-th Fibonacci number

def precomput(f):
    # 0th and 1st number of the series
    # are 0 and 1
    f.append(0)
    f.append(1)


    # Add the previous 2 numbers in the series
    # and store last two digits of result
    for i in range(2, 300):
        f.append((f[i - 1] + f[i - 2]) % 100)

    # Returns last two digits of


# n'th Fibonacci Number
def findLastDigit(f, n):
    return f[n % 300]


# driver code
f = list()
precomput(f)
# n = 1
# print(findLastDigit(f, n))
# n = 61
# print(findLastDigit(f, n))
# n = 7
# print(findLastDigit(f, n))
n = 350
print(findLastDigit(f, n))

# This code is contributed by "Abhishek Sharma 44"
