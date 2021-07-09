from random import random

data = []


def random_values(arr):
    for i in range(10):
        arr.append(int(random()*100))

    return arr


print(random_values(data))


def quicksort(arr):

    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr.pop()
    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


print(quicksort(data))
