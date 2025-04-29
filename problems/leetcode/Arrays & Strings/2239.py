from typing import List

# 2239. Find Closest Number to Zero
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minimum_value = nums[0]
        minimum_difference = abs(nums[0])
        for current_value in nums:
            # Update minimum_value if we find a smaller absolute value
            if abs(current_value) < minimum_difference:
                minimum_value = current_value
                minimum_difference = abs(current_value)
            # If there's a tie in absolute values, pick the larger value
            elif (abs(current_value) == minimum_difference) and (current_value > minimum_value):
                minimum_value = current_value
        return minimum_value

# Test cases
def test():
    sol = Solution()

    test_cases = [
        ([2, -1, 1], 1),  # Expected result: 1
        ([-4, -2, 1, 4, 8], 1),  # Expected result: 1
        ([0, -1, 1], 0),  # Expected result: 0
        ([-5, -3, -1], -1),  # Expected result: -1
        ([3, 7, 8], 3),  # Expected result: 3
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.findClosestNumber(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")
        print('-' * 50)

if __name__ == "__main__":
    test()