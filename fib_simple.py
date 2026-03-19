# Simple Fibonacci: The Pythonic Way
# Date: 2026-03-19
# Complexity: O(n) Time, O(1) Space

def fib_simple(n):
    """
    Calculates the nth Fibonacci number efficiently.
    Uses variable swapping to avoid recursion and lists.
    """
    a, b = 0, 1
    for _ in range(n):
        # Pythonic swap: a becomes b, and b becomes the sum (a + b)
        a, b = b, a + b
    return a

if __name__ == "__main__":
    n = 100
    print(f"The {n}th Fibonacci number is: {fib_simple(n)}")
    # This finishes instantly, unlike the recursive version!
