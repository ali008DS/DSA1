'''
 ****Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

</aside>'''
def remove_element(nums, val):
    i = 0
    k = 0
    
    while i < len(nums):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        i += 1

    return k

# Example usage:
nums = [3, 2, 2, 3]
val = 3
result = remove_element(nums, val)
print("Output:", result, ", nums =", nums[:result], "_*")