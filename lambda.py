add = lambda x, y: x + y
print(add(3, 6))

is_even = lambda x: x if x%2 == 0 else False
print (is_even(41))

def add_n(n):
    return lambda x: x + n

add2 = add_n(2)
print(add2(3))
