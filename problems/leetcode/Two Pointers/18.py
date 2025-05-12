from typing import List

# 18. 4Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # we sort the array O(n log n) to maintain order,
        # as movement of pointers depend on the difference of the sum to target.
        # we will fix the first number, then the second number, in two nested loops.
        # the third number is a moving pointer, and the fourth number is a moving pointer.
        # the moving pointers depend on the difference of the sum to target.
        # in case the sum of 4 digits is >target; we lower the right pointer.
        # if it is <target; we move the left pointer.
        # otherwise we append the quadruplets as a result.
        # sorting helps us to not duplicate out answers by only using elements once.
        # it also allows efficient parsing;
        # as we always start from the index after the other fixed digits;
        # minimizing the access of duplicate & useless parses.
        # rest of the duplicates are also checked after appending a result set.

        nums.sort()
        answer = []
        length = len(nums)

        for f in range(length):

            if f > 0 and nums[f] == nums[f - 1]:
                continue

            for i in range(f + 1, length):

                if i > f + 1 and nums[i] == nums[i - 1]:
                    continue

                j = i + 1
                k = length - 1

                while j < k:
                    if nums[f] + nums[i] + nums[j] + nums[k] > target:
                        k -= 1
                    elif nums[f] + nums[i] + nums[j] + nums[k] < target:
                        j += 1
                    else:
                        answer.append([nums[f], nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1

                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1

        return answer

# Test function
def test():
    sol = Solution()
    
    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2],[-2, 0, 0, 2],[-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.fourSum(nums, target)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()