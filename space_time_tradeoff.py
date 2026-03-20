# The Space-Time Trade-off
# Date: 2026-03-19

import time

# PROBLEM: We want to check if a specific ID exists in a list of 100,000 IDs.

def slow_search_zero_space(target, data_list):
    """
    TRADEOFF: This saves SPACE.
    It uses NO extra memory (O(1) space).
    But it is SLOW (O(n) time) because it checks every item one by one.
    """
    for item in data_list:
        if item == target:
            return True
    return False

def fast_search_high_space(target, data_set):
    """
    TRADEOFF: This saves TIME.
    It is INSTANT (O(1) time) because it uses a 'Hash Set'.
    But it uses EXTRA MEMORY (O(n) space) to store that set in RAM.
    """
    return target in data_set

if __name__ == "__main__":
    # Create a list of 100,000 numbers
    large_list = list(range(100000))
    # Create a set from that list (This is the "Space" we are spending)
    large_set = set(large_list)
    
    target_number = 99999 # The very last number
    
    # Measure Slow Search
    start = time.time()
    slow_search_zero_space(target_number, large_list)
    print(f"Slow Search (O(1) Space, O(n) Time): {time.time() - start:.6f} seconds")
    
    # Measure Fast Search
    start = time.time()
    fast_search_high_space(target_number, large_set)
    print(f"Fast Search (O(n) Space, O(1) Time): {time.time() - start:.6f} seconds")

    print("\nCONCLUSION:")
    print("The Fast Search is nearly instant because we 'spent' memory to create the Set.")
    print("The Slow Search is slower because we refused to use extra memory.")
