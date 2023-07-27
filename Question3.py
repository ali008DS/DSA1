'''
💡  Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2

</aside>'''
def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # At this point, left is the index where the target would be inserted
    return left

# Example 1
nums = [1, 3, 5, 6]
target = 5
result = search_insert(nums, target)
print(result)  # Output: 2 (Index of the target value 5 in the given sorted array)