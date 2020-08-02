from random import randint


def merger(a, b):
    new_list = []
    d = a + b
    while d:
        delete_num = min(d)
        while delete_num in d:
            new_list.append(delete_num)
            d.remove(delete_num)
    return new_list


list1 = [randint(1, 30) for i in range(5)]
list2 = [randint(1, 30) for i in range(5)]
list2.sort()
list_c = merger(list1, list2)
print(list_c)
