# call by value
string = "call by value"
def test(string):
    string = string+'\t' + "call_by_value_of_the_string"
    print("Inside function:\t", string)
test(string)
print("outside function:\t", string)

# call_by_ref
# list1 = [10, 20, 30, 40]
def numlist(list1):
    list1.append(50)
    print("inside func:\t", list1)
    return list1

mylist = [10,20,30,40,60]
numlist(mylist)
print("outside the func\t", mylist)

