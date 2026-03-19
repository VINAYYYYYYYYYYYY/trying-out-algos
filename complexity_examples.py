# Complexity Examples: Square vs. Exponential
# Date: 2026-03-19

# 1. Square Algorithm: O(n^2) - Bubble Sort
# Properties: 
# - Uses a "nested loop" (a loop inside a loop).
# - The inner loop (j) must complete all its cycles before the outer loop (i) moves one step.
# - Efficiency: For n=100 items, it does 10,000 operations.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # n-i-1: -1 prevents 'out of bounds' error, -i skips already sorted ends
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]: # The Comparison
                # The Swap: "Bubbles" the larger number to the right
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 2. Exponential Algorithm: O(2^n) - Recursive Fibonacci
# Properties:
# - Uses recursion where the function calls itself TWICE.
# - The workload doubles with every single increase in 'n'.
# - Efficiency: For n=100, this would take billions of years to finish.
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test cases
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {sample_list}")
    print(f"Sorted (Bubble Sort): {bubble_sort(sample_list)}")
    print(f"Fibonacci(7): {fibonacci_recursive(7)}")
