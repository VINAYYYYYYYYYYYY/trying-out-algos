# Space Complexity: O(1) vs. O(n)
# Date: 2026-03-19

# 1. Constant Space: O(1)
# The amount of extra memory used does NOT grow with the input.
def find_max_constant_space(numbers):
    # We only create ONE extra variable ('max_val') 
    # regardless of whether the list has 10 or 10,000,000 items.
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

# 2. Linear Space: O(n)
# The amount of extra memory used grows EXACTLY like the input.
def double_numbers_linear_space(numbers):
    # We create a BRAND NEW list that is the same size as the input.
    # If the input has 1,000,000 items, this function uses 
    # 1,000,000 items worth of EXTRA RAM.
    new_list = []
    for num in numbers:
        new_list.append(num * 2)
    return new_list

if __name__ == "__main__":
    test_data = [1, 2, 3, 4, 5]
    
    print("O(1) Space Example: Finding max doesn't need extra lists.")
    print(f"Max: {find_max_constant_space(test_data)}")
    
    print("\nO(n) Space Example: Doubling the list creates a full copy in RAM.")
    print(f"Doubled: {double_numbers_linear_space(test_data)}")
