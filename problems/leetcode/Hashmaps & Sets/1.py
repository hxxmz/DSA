from typing import List

# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Time: O(n)
        # Space: O(n)

        # we iterate through the array;
        # looking for the pair of the number in the hashmap.
        # in case the pair is not found in the hashmap;
        # we store the current number with its index in the hashmap;
        # to act as a future lookup pair.

        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.twoSum(nums, target)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()