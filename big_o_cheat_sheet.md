# Big O Cheat Sheet: Time & Space
# Date: 2026-03-19

Big O notation is a mathematical model used to predict how an algorithm scales. It focuses on the **Worst-Case Scenario**.

## 1. Time Complexity (Execution Speed)
How the number of operations grows relative to the input size ($n$).

| Notation | Name | Speed | Example |
| :--- | :--- | :--- | :--- |
| **O(1)** | Constant | Instant | Accessing an array index |
| **O(log n)** | Logarithmic | Very Fast | Binary Search |
| **O(n)** | Linear | Fast | Single loop through a list |
| **O(n log n)** | Linear-Log | Good | Efficient sorting (Merge/Quick Sort) |
| **O(n^2)** | Quadratic | Slow | Nested loops (Bubble Sort) |
| **O(2^n)** | Exponential | Terrible | Recursive Fibonacci / Power Set |

## 2. Space Complexity (Memory Usage)
How much extra memory is needed as the input size ($n$) grows.

*   **O(1) Space:** You use a fixed amount of memory (like 2 variables) regardless of how big the input is.
*   **O(n) Space:** You create a new list or structure that is the same size as your input.

## Summary
- **Big O** = Scaling (Growth).
- **Time** = Operations (CPU).
- **Space** = Memory (RAM).
