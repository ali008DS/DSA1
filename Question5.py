'''
💡 You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

</aside>'''
def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array.
    p1, p2, p3 = m - 1, n - 1, m + n - 1

    # Merge nums1 and nums2 starting from the end of each array.
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1

    # If there are remaining elements in nums2, copy them to nums1.
    while p2 >= 0:
        nums1[p3] = nums2[p2]
        p2 -= 1
        p3 -= 1

# Example usage:
nums1 = [1, 3, 5, 0, 0, 0]  # The length is m + n = 6
nums2 = [2, 4, 6]  # The length is n = 3
m = 3
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 3, 4, 5, 6]