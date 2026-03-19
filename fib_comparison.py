# Fibonacci: Exponential (Bad) vs. Linear (Good)
# Date: 2026-03-19

# EXPONENTIAL: O(2^n)
# Purpose: Educational. Shows how recursion can "explode" in complexity.
# Why it's bad: It repeats work. fib(5) calculates fib(3) multiple times.
def fib_exponential(n):
    if n <= 1:
        return n
    return fib_exponential(n - 1) + fib_exponential(n - 2)

# LINEAR: O(n)
# Purpose: Real-world calculation.
# Why it's good: It calculates each number only ONCE and stores it.
def fib_linear(n):
    if n <= 1:
        return n
    fib_list = [0, 1]
    for i in range(2, n + 1):
        # Just add the last two numbers in the list
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    return fib_list[n]

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci of {n}:")
    print(f"- Exponential O(2^n) result: {fib_exponential(n)}")
    print(f"- Linear O(n) result:      {fib_linear(n)}")
    
    # Try n=40 and you will see the Exponential version start to lag!
