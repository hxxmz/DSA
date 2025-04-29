from typing import List

# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(n)
        # if the length of set of the number is equal to the numbers itself;
        # it doesn't contain any duplicate values.
        return len(set(nums)) != len(nums)

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([99], False),
        ([], False)
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.containsDuplicate(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()