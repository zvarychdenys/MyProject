from random import random

data = []


def random_values(arr):
    for elem in range(15):
        arr.append(int(random()*100))

    return arr


print(random_values(data))


def selecion_sort(arr):

    n = len(arr)

    for elem in range(n):
        min_value = elem

        for i in range(elem+1, n):
            if arr[min_value] > arr[i]:
                min_value = i

        arr[elem], arr[min_value] = arr[min_value], arr[elem]

    return arr


print(selecion_sort(data))
