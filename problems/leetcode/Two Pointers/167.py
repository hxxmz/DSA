from typing import List

# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Start from the beginning and end.
        # if target < sum of two pointer values, r -= 1 (shrink the sum by lowering high value)
        # if target > sum then we need greater left value to level the sum
        # return index + 1 (1-indexed array of integers) of both values that add to the target
        # it is guaranteed that there's a result, "there is exactly one solution"

        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target: # can be else just here for clarity
                l += 1

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([1, 2], 3, [1, 2]),
    ]

    for i, (numbers, target, expected) in enumerate(test_cases):
        result = sol.twoSum(numbers, target)
        print(f"Test case {i+1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()