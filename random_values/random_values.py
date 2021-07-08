from random import random

list1 = []

amount = (int(input("How many numbers do you want?")))
n = (int(input("What range do you want?")))


def random_values(arr, x, rang):
    if x <= 0:
        print("Please write a number greater than 0")

    else:
        for i in range(x):
            arr.append(int(random()* rang))

        return arr


print(random_values(list1, amount, n))
