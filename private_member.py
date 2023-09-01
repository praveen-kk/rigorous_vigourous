# base class
class company:
    def __init__(self):
        # protected member
        self._project = 'openGov'

# child class
class Employee(company):
    def __init__(self, name):
        self.name = name
        company.__init__(self)

    def show(self):
        return self.name, self._project


c = Employee("johnny")
print(c.show())



#####################################################
# class company:
#     def __init__(self):
#         # protected member
#         self._project = 'openGov'
#
#
# # child class
# class Employee(company):
#     def __init__(self, name):
#         self.name = name
#         company.__init__(self)
#
#     def show(self):
#         return self.name, self._project
#
#
# c = Employee("johnny")
# print(c.show())
