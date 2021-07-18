from random import random

data = []


def random_values(arr):
    for elem in range(15):
        arr.append(int(random()*100))

    return arr


print(*random_values(data))


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    if i < len(left):
        sorted_list += left[i:]
        i += 1

    if j < len(right):
        sorted_list += right[j:]

    return sorted_list


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(*merge_sort(data))