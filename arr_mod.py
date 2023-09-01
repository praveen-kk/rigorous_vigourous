def change(array, modulus):
    # x = lambda x: x[::-1][:array] + x[modulus]
    # return x
    return lambda x: x[::-1][:array] + x[modulus]


array1 = [1, 3, 5, 7, 9, 11]
modulus1 = 3
print(change(array1, modulus1))
