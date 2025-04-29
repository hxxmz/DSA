from typing import List

# 75. Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time: O(n)
        # Space: O(1)

        # we count all of the colors and their count in the first iteration.
        # we replace the nums in-place according to their count.

        colors = {}
        for color in nums:
            if color not in colors:
                colors[color] = 1
                continue
            colors[color] += 1
        
        current = 0
        for i in range(len(nums)):
            if colors[current] == 0:
                current += 1
            nums[i] = current
            colors[current] -= 1

        print(nums)

    def DutchNationalFlagAlgorithm(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time: O(n)
        # Space: O(1)

        # three pointers that check the actual place of the element.
        # DNF only works for an array with 3 unique elements.

        left, right = 0, len(nums)-1
        current = 0
        
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left +=1
                current += 1
            elif nums[current] == 1:
                current += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1

        print(nums)

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([2, 0, 2, 1, 1, 0], "sortColors", [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], "sortColors", [0, 1, 2]),
        ([2, 0, 2, 1, 1, 0], "DutchNationalFlagAlgorithm", [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], "DutchNationalFlagAlgorithm", [0, 1, 2]),
    ]

    for i, (nums, method, expected) in enumerate(test_cases):
        if method == "sortColors":
            sol.sortColors(nums)
        elif method == "DutchNationalFlagAlgorithm":
            sol.DutchNationalFlagAlgorithm(nums)
        
        print(f"Test case {i + 1}: {'✅' if nums == expected else '❌'} | Output: {nums} | Expected: {expected}")

if __name__ == "__main__":
    test()