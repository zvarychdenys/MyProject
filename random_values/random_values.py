
from random import random


class Random():

    list1 = []

    def __init__(self):
        self.numb = (int(input("How many numbers do you want?")))
        self.range = (int(input("What range do you want?")))

    def random_values(self):
        if self.numb <= 0:
            print("Please write a number greater than 0")

        else:
            for i in range(self.numb):
                self.list1.append(int(random() * self.range))

            return self.list1


r = Random()
print(r.random_values())
