def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

data = [10, 20, 30, 'invalid']  # Mixed type issue
try:
    avg = calculate_average(data)
    print(avg)
except TypeError:
    print("Type mismatch!")
