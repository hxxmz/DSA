from typing import List
# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]:
                return nums[m + 1]
            elif nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

        return nums[l]

# Test Function
def test():
    sol = Solution()
    
    test_cases = [
        ([3, 4, 5, 1, 2], 1),             # Rotated, minimum is 1
        ([4, 5, 6, 7, 0, 1, 2], 0),       # Rotated, minimum is 0
        ([11, 13, 15, 17], 11),           # Not rotated, minimum is 11
        ([2, 1], 1),                      # Two elements rotated, minimum is 1
        ([1], 1),                         # Single element, minimum is itself
        ([2, 3, 4, 5, 6, 7, 1], 1),       # Rotated, minimum is 1
        ([5, 6, 7, 8, 9, 1, 2, 3, 4], 1), # Rotated, minimum is 1
        ([1, 2, 3, 4, 5], 1),             # Already sorted, minimum is 1
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.findMin(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()