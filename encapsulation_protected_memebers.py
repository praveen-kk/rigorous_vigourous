class Base:
    def __init__(self):
        # protected member
        self._a = 2


# creating a derived class
class Derived(Base):
    def __int__(self):
        #         calling constructor of base class
        Base.__init__(self)
        print("calling protected member of base class:", self._a)
        # modify protected variable
        self._a = 3


obj1 = Derived()
obj2 = Base()
# print accessing protected member of  obj1
print("print accessing protected member of  obj1----", obj1._a)
print("accessing protected member of obj2------", obj2._a)
