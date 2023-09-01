class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


class test(Employee):
    def __int__(self):
        print(self.name)

emp = Employee('star', 3000000)
print(test(emp))
# if __name__ == '__main__':
#     print(test)