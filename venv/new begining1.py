from array import *
array1 = array ('i', [1, 10, 20, 30, 40 ])
# for x in array1:
#     print(x)
array2 = list(map(lambda x: x if(x > 20 or x == 20 ) else array1.remove(x), array1))

print(array2)

# nums = [1, 2, 3, 4, 5, 6, 7]
# sq = list(map(lambda a: a*a, nums))
# print(sq)