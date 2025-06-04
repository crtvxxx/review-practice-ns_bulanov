def calculate_positive_average(numbers: list[float | int]) -> float:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")
    total = 0.0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
            count += 1
    return total / count if count > 0 else 0.0
