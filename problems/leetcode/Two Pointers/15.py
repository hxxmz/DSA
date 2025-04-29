from typing import List

# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # we sort the array O(n log n) to maintain order,
        # as movement of pointers depend on the difference of the sum to 0.
        # in case the sum of 3 digits is >0; we lower the right pointer.
        # if it is <0; we move the left pointer.
        # otherwise we append the triplet as a result.
        # sorting helps us to not duplicate out answers by only using elements once.
        # it also allows efficient parsing;
        # as we always start from the index after the fixed third digit;
        # minimizing the access of duplicate & useless parses.
        # rest of the duplicates are also checked after appending a result set.

        nums.sort()
        answer = []
        length = len(nums)

        for i in range(length):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = length - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    answer.append([nums[i], nums[j], nums[k]])
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
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.threeSum(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()
