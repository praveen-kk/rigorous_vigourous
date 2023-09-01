# A set of disks numbered  through  are placed in a line in random order.
#
# What is the probability that we have a partial derangement such that exactly  prime number discs are found away from their natural positions? (Any number of non-prime disks may also be found in or out of their natural positions.)
#
# It can be shown that for a given constraints the answer can be represented as , where  and  are coprime positive integers and . Print the value of  modulo .
#
# Input Format
#
# The only line of input contains two integers  and  separated by single space.
#
# Constraints
#
#  where  is number of primes in range from  to  inclusive.
# Output Format
#
# Print the only line with the answer.
#
# Sample Input 0
#
# 10 3
# Sample Output 0
#
# 498412760
# Explanation 0
#
# The actual value of  is .

#how to identify the prime number
from itertools import count, filterfalse

a = [99, -3, 4, 5, 33, 44, 55, 77, 88]
b=iter(a)

# print(next(b))
for index in range(3):
     print(next(b, 1))
# for i in count(10,3):
#     print(i)
#     if i > 20:
#         break
print(filterfalse(set(a).__contains__,count(1)))