'''
💡  ****You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]

</aside>'''
def moveZeroes(nums):
    # Initialize the pointer to keep track of the next position for nonzero elements
    next_nonzero = 0

    # Traverse the array with the pointer `i`
    for i in range(len(nums)):
        # If the current element is nonzero, move it to the `next_nonzero` position
        if nums[i] != 0:
            nums[next_nonzero] = nums[i]
            # Increment the `next_nonzero` pointer
            next_nonzero += 1

    # After processing all elements, set all elements from `next_nonzero` to the end of the array as 0
    for i in range(next_nonzero, len(nums)):
        nums[i] = 0

# Test the function with the given example
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]