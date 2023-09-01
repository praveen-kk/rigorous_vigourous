# def solution(N):
#     lst=list(str(N))
#     l=len(n)
#     if N > 0:
#         for i,n in enumerate(lst):
#             if
#             temp=n.pop(i)
#             b=
#             if n(i)>5:
#                 continue
#             else:
#                 i=5
#             int(a).append(i)
#
#     # else:
#     #     for i in n:
#     #         a=i
#     #         if int(i)<5:
#     #             continue
#     #         else:
#     #             i=5
#     #         int(a).append(i)
#     return a
#
# print(solution(268))
#
#
# # def solution(N):
# #     while(N>0):
#
# # def solution(N):
# #     for i in N:
# #
#
# 778665
# 543456
# -57765
#

import itertools
def solution(N):
    lst=list(str(abs(N)))
    if N>0:
        result=itertools.dropwhile(lambda x: int(x)>5, lst)
    elif N<0:
        result = itertools.dropwhile(lambda x: int(x)<5, lst)
    a=[]
    for i in range(len(lst)):
        if N>0:
            if int(lst[i])<5:
                a.append("5")
                # a.append(lst[i])
                
        elif N<0:
            print(int(lst[i]))
            if int(lst[i])>=5:

                # a.append(lst[i])
                a.append("5")
                print(a)
                break

        a.append(lst[i])
    for each in result:
        a.append(each)
        print(each)

    if N>0:
        return int("".join(map(str, a)))
    else:
        return -(int("".join(map(str, a))))
print(solution(99))
    # for i in lst:
    #     if int(i)<5:

