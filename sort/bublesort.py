from random import random

data = []


def random_values(arr):
    for elem in range(15):
        arr.append(int(random()*100))

    return arr


print(random_values(data))


def buble_sort(arr):

    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(buble_sort(data))