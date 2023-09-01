# txt = "apple, banana, cherry"
#
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# # x = txt.rsplit(",", 1)
#
# print(txt.rstrip(","))

# # multi line string
# grocery = '''Milk
# Chicken
# Bread
# Butter'''
#
# print(grocery.splitlines(True))

def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return  modified_result
    return wrapper

@uppercase_decorator
def greet():
    return "use decorators"
print(greet())

#############################################################################

#how to retrieve counts of ip address from log file 