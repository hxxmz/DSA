from typing import List

# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        
        return -1

# Test Function
def test():
    sol = Solution()
    
    # Test Cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 4, 3),               # Target exists in the middle
        ([1, 2, 3, 4, 5, 6], 1, 0),               # Target is the first element
        ([1, 2, 3, 4, 5, 6], 6, 5),               # Target is the last element
        ([1, 2, 3, 4, 5, 6], 7, -1),              # Target is not present
        ([], 1, -1),                              # Empty list, target not found
        ([5], 5, 0),                              # Single-element list, target found
        ([5], 1, -1),                             # Single-element list, target not found
        ([1, 3, 5, 7, 9, 11, 13], 11, 5),         # Odd length list
        ([2, 4, 6, 8, 10, 12, 14], 8, 3),         # Even length list
    ]

    for i, (nums, target, expected_output) in enumerate(test_cases):
        result = sol.search(nums, target)
        print(f"Test case {i + 1}: {'✅' if result == expected_output else '❌'} | Output: {result} | Expected: {expected_output}")

if __name__ == "__main__":
    test()