import time
import random

# 1. Square Algorithm: O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 2. Linear-Logarithmic Algorithm: O(n log n) - Built-in Python Sort
# This is what you SHOULD use for Big Problems.
def fast_sort(arr):
    return sorted(arr)

def run_benchmarks(input_size):
    print(f"\n--- TESTING INPUT SIZE: n = {input_size} ---")
    
    # Generate random data
    data = [random.randint(0, 1000) for _ in range(input_size)]
    
    # Test Fast Sort
    start_time = time.time()
    fast_sort(data.copy())
    fast_end = time.time() - start_time
    print(f"Fast Sort O(n log n): {fast_end:.6f} seconds")
    
    # Test Bubble Sort
    # WARNING: We don't run Bubble Sort on huge numbers because it would take hours!
    if input_size <= 10000:
        start_time = time.time()
        bubble_sort(data.copy())
        bubble_end = time.time() - start_time
        print(f"Bubble Sort O(n^2):  {bubble_end:.6f} seconds")
        
        # Calculate the ratio
        if fast_end > 0:
            print(f"Result: Bubble Sort was {bubble_end/fast_end:.1f}x slower than Fast Sort!")
    else:
        print("Skipping Bubble Sort... it would take too long for this input size!")

if __name__ == "__main__":
    # SMALL PROBLEM
    run_benchmarks(100)
    
    # MEDIUM PROBLEM
    run_benchmarks(1000)
    
    # BIG PROBLEM (The Wall)
    run_benchmarks(10000)
    
    print("\nCONCLUSION:")
    print("Notice how for n=100, the difference is tiny.")
    print("But when n increases 100x (to 10,000), the Square algorithm becomes MASSIVELY slower.")
