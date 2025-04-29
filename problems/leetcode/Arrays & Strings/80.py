from typing import List

# 80. Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # We initialize the pointer `l` at 2, as we can have at most two occurrences of each element.
        # On every left element that is not the same as the right element, we replace the elements;
        # keeping the third one in the line unique, moving l pointer forward to check the next element.

        l = 2
        for r in range(2, len(nums)):
            if nums[r] != nums[l-2]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        print(nums)
        return l

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], 5),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.removeDuplicates(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected} | nums after modification: {nums[:result]}")

if __name__ == "__main__":
    test()