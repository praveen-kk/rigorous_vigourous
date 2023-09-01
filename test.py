# def sort_list_using_another(list1, list2):
#     print(list(zip(list2, list1)))
#     combined = list(zip(list2, list1))
#     print(combined.sort())  # Sort based on list2 values
#     sorted_list = [item[1] for item in combined]
#     return sorted_list
#
# # Given input lists
# list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
# print (sort_list_using_another(list1, list2))


def sort_list(list1, list2):
    result = dict(sorted(zip(list1, list2), key = lambda item: item[1]))
    l3 = []
    for key in result:
        l3.append(key)

    return l3

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print(sort_list(list1, list2))