from memory_profiler import profile

@profile
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(range(1, 10000001))  # Большой массив для теста
target = 10000000
linear_search(arr, target)
