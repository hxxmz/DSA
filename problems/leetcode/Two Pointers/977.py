from typing import List

# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # initially i started with squaring the array in-place,
        # rearranging the values by swapping using two pointers
        # BUT a better approach is to populate & rearrange using two pointers at the same time.
        # we know that the two ends would always have extreme squares, so we compare and pick larger;
        # moving pointers away from the elements used, and squaring them as we place them.

        length = len(nums)
        l, r = 0, length - 1
        resultant_array = [None] * length
        resultant_arr_ptr = length - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                resultant_array[resultant_arr_ptr] = nums[r] ** 2
                r -= 1
            else:
                resultant_array[resultant_arr_ptr] = nums[l] ** 2
                l += 1
            resultant_arr_ptr -= 1

        return resultant_array

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([-5, -3, -2, -1], [1, 4, 9, 25]),
        ([0, 2, 3], [0, 4, 9]),
        ([1], [1]),
        ([0], [0]),
        ([], []),
        (list(range(-1000, 1001)), sorted([x*x for x in range(-1000, 1001)])),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.sortedSquares(nums)
        print(f"Test case {i+1}: {'✅' if result == expected else '❌'} | Output: {result[:10]}{'...' if len(result) > 10 else ''} | Expected: {expected[:10]}{'...' if len(expected) > 10 else ''}")

if __name__ == "__main__":
    test()