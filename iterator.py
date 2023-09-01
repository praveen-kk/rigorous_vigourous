# mylist = [9, 1, 4]
# iterator = iter(mylist)
# print(next(iterator))
# print(next(iterator))
# while x in range(len(mylist)):
#     print(next(iterator))
#     until:
#     x = 0
# for iterator in iter(mylist):
#     print(next(iterator))

def summming(*args):
    result = 0
    for value in args:
        result += value
    return result
print(summming(3, 4, 7, 8, 10, 14))

string: str = 'string'
t: tuple[int | str, ...] = (1, 2, 4, 5, 'a', 'b')

a = [1, 2, 3]
b = a.copy()

b.extend([9, 4, 5, 6])
print(a, b)

def func(key, value, d={}):
    d[key] = value
    return d
print(func('a', 9))
print(func('b', 11))



