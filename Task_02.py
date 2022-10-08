# 2. Дан список чисел. Создайте список, в который попадают числа,
#    описываемые возрастающую последовательность.
#    Порядок элементов менять нельзя.
# in  8  >> out  [10, 0, 5, 11, 6, 1, 15, 10]
#        >>      [[10, 11, 15], [0, 5, 11, 15], [5, 11, 15]],
#        >>       [11, 15], [6, 15], [1, 15]]
# in  10 >> out  [[19, 5, 1, 14, 5, 9, 15, 11, 12, 2]]
#        >>      [[5, 14, 15], [1, 14, 15], [14, 15],
#        >>       [5, 9, 15], [9, 15], [11, 12]]

from random import choices


def sequ(num):
    if num < 1:
        return []
    return choices(range(num * 2), k=num)


def all_sets(num_list):
    new_list = []
    for k in range(len(num_list)):
        n = num_list[k]
        temporary = [n]
        for i in range(k + 1, len(num_list)):
            if num_list[i] > n:
                temporary.append(num_list[i])
                n = num_list[i]
        if len(temporary) > 1:
            new_list.append(temporary)

    return new_list


list_nums = sequ(int(input()))
print(list_nums)
print(all_sets(list_nums))
