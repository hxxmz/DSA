from typing import List

# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        return l

# Test Function
def test():
    sol = Solution()
    
    # Test Cases
    test_cases = [
        ([1, 3, 5, 6], 5, 2),     # Target exists in the middle
        ([1, 3, 5, 6], 2, 1),     # Target does not exist, should be inserted at index 1
        ([1, 3, 5, 6], 7, 4),     # Target is greater than all elements, should be inserted at the end
        ([1, 3, 5, 6], 0, 0),     # Target is less than all elements, should be inserted at the start
        ([], 5, 0),               # Empty list, should be inserted at the start
        ([1], 1, 0),              # Single-element list, target matches
        ([1], 0, 0),              # Single-element list, target smaller
        ([1], 2, 1),              # Single-element list, target larger
        ([1, 2, 4, 6, 7], 3, 2),  # Target should be inserted between 2 and 4
        ([1, 2, 4, 6, 7], 4, 2),  # Target matches element at index 2
    ]

    for i, (nums, target, expected_output) in enumerate(test_cases):
        result = sol.searchInsert(nums, target)
        print(f"Test case {i + 1}: {'✅' if result == expected_output else '❌'} | Output: {result} | Expected: {expected_output}")

if __name__ == "__main__":
    test()