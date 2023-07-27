''''
💡  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

</aside>'''
def containsDuplicate(nums):
    # Create an empty set to keep track of unique elements
    unique_elements = set()

    # Traverse through the array
    for num in nums:
        # If the current element is already in the set, it's a duplicate
        if num in unique_elements:
            return True
        # Otherwise, add it to the set
        unique_elements.add(num)

    # If no duplicates were found, return False
    return False

# Example usage:
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)  # Output: True