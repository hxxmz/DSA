from typing import List

# 228. Summary Ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums: return []

        if len(nums) == 1:
            return [str(nums[0])]

        start = str(nums[0])

        result = []
        
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue

            if start != str(nums[i-1]):
                start += "->" + str(nums[i-1])

            result.append(start)
            start = str(nums[i])
        
        if start != str(nums[i]):
                start += "->" + str(nums[i])

        result.append(start)

        return result

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
        ([], []),
        ([5], ["5"]),
        ([1, 2, 3, 4], ["1->4"]),
        ([1, 3, 5, 7], ["1", "3", "5", "7"]),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.summaryRanges(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()
