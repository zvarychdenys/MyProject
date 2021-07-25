arr = [2, 3, -3, 43, 234, -2, 5]
target = 5
print("Array before sorted : ", arr)

arr.sort()  # binary search is only possible with sorted array
print("Array after  sorted : ", arr)

print("Own target is : ", target)


def binary_search(data, goal):
    lowest = 0
    highest = len(data) - 1
    index = None  # index target

    while (lowest <= highest) and (index is None):
        mid = (lowest + highest) // 2
        if data[mid] == goal:
            index = mid
        else:
            if goal < data[mid]:
                highest = mid - 1
            else:
                lowest = mid + 1

    print("Target,", goal, "has index ", index)


binary_search(arr, target)
