from typing import List

# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: # dry approach
        l = 0
        r = 1

        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]

            nums[r] = "_"
            r += 1

        print(nums)
        return l+1

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.removeDuplicates(nums)
        print(f"Test case {i + 1}:")
        print(f"  Output: {result} | Expected: {expected} {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    test()