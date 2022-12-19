number = 10000
data = list(range(0, number, 3))
target = 9999


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


def iter_binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def recur_binary_search(data, target, low, high):
    # print(low, high)
    if low > high:
        return False

    mid = (low + high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return recur_binary_search(data, target, low, mid - 1)
    else:
        return recur_binary_search(data, target, mid + 1, high)


print(linear_search(data,target))
print(iter_binary_search(data, target))
print(recur_binary_search(data, target, 0, len(data)-1))
#
# import timeit
# n = 15
# result = timeit.timeit(stmt='linear_search(data,target)', globals=globals(), number=n)
# print(f"Execution time is {result / n} seconds")
# result = timeit.timeit(stmt='iter_binary_search(data, target)', globals=globals(), number=n)
# print(f"Execution time is {result / n} seconds")
# result = timeit.timeit(stmt='recur_binary_search(data, target, 0, len(data)-1)', globals=globals(), number=n)
# print(f"Execution time is {result / n} seconds")
