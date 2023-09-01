# You are given a function . You are also given  lists. The  list consists of  elements.
#
# You have to pick one element from each list so that the value from the equation below is maximized:
#
# %
#
#  denotes the element picked from the  list . Find the maximized value  obtained.
#
#  denotes the modulo operator.
#
# Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
#
# Input Format
#
# The first line contains  space separated integers  and .
# The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.
#
# Constraints
#
#
#
#
#
# Output Format
#
# Output a single integer denoting the value .
#
# Sample Input
#
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
# Sample Output
#
# 206
# Explanation
#
# Picking  from the st list,  from the nd list and  from the rd list gives the maximum  value equal to % = .
import itertools
def soultion():
    k, m=map(int, input().split())
    n=(list(map(int, input().split()))[1:] for _ in range(k))
    print(max(map(lambda x: sum(i**2 for i in x)%m, itertools.product(*n))))
list = [23, 5, 65, 3, 2, 2, 45, 8]
soultion(list)
    # for each in N:
    #     sum=+max(each).__pow__(2)
    #     l=map(lambda )
    # return sum%m



