# Exponential Algorithm Example: Generating a Power Set
# Date: 2026-03-19
# Complexity: O(2^n) - Every new element doubles the amount of work.

def generate_power_set(input_set):
    """
    This algorithm finds every possible subset of a given list.
    It is O(2^n) because the number of subsets is 2 raised to the 
    power of the number of elements in the input list.
    """
    subsets = [[]]  # Start with the empty set
    
    for element in input_set:
        # For every existing subset, we create a NEW one that includes the new element
        new_subsets = []
        for current_subset in subsets:
            new_subsets.append(current_subset + [element])
        
        # Add the new subsets to our total list (this is where it doubles!)
        subsets.extend(new_subsets)
        
    return subsets

if __name__ == "__main__":
    # Small example
    items = ["Apple", "Banana", "Cherry"]
    result = generate_power_set(items)
    
    print(f"Input Set: {items}")
    print(f"Number of subsets (2^3): {len(result)}")
    print("All subsets:")
    for subset in result:
        print(f" - {subset}")
    
    # Warning: Do not try this with a list of 100 items! 
    # Your computer will run out of memory.
