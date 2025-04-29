from typing import List

# 18. 4Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass

# Test function
def test():
    sol = Solution()
    
    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.fourSum(nums, target)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()