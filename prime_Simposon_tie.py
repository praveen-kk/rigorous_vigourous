# Given an integer, if the number is prime,
# return 1. Otherwise, return its smallest divisor greater than 1.

# def prime_num(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#
#         # return (lambda n: next((i for i in range(2, n) if n % i == 0), 1))
#
#         for i in range(2, n):
#             if n % i == 0:
#                 return i
#                 break
#         else:
#             return 1


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

number = 1000000000000066600000000000001  # Replace with your desired number
result = is_prime(number)
print(result)

# print(prime_num(3857))

# import time
#
#
# def measure_execution_time(func, *args, **kwargs):
#     start_time = time.time()
#     result = func(*args, **kwargs)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"Time taken to execute {func.__name__}: {elapsed_time:.6f} seconds")
#     return result


# Usage example

# my_lambda = lambda x: x ** 2
# measure_execution_time(is_prime(7))
