def sum_list(items):
    """Simple sum function – no validation."""
    total = 0
    for item in items:
        total += item
    return total

# Test usage
numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(f"Sum: {result}")

# Edge case (should error or handle)
empty_result = sum_list([])
print(f"Empty sum: {empty_result}")  # Will be 0, but no check

# Potential issue: Non-numeric input
mixed = [1, 2, "three", 4]  # TypeError on run, but static review catches
try:
    mixed_sum = sum_list(mixed)
    print(f"Mixed sum: {mixed_sum}")
except TypeError:
    print("Error: Mixed types!")
