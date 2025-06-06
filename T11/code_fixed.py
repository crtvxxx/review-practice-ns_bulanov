def factorial(n):
    result = 1
    for i in range(1, n + 1): 
        result *= i
    return result

def calculate_sum(arr):
    total = 0
    for i in range(0, len(arr)):
        total += arr[i]
    return total

numbers = [10, 20, 30]
print(calculate_sum(numbers))  # Теперь возвращает 60
print(factorial(5))  # Теперь возвращает 120
