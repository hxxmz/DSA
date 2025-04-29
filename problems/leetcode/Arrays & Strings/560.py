from typing import List

# 560. Subarray Sum Equals K
class Solution:
    def subarraySum(nums, k: int) -> int:
        length = len(nums)
        
        prefix_sum = [0] * length
        summ = 0
        for i in range(length):
            summ += nums[i]
            prefix_sum[i] = summ

        print(prefix_sum)

        answer = 0


        return answer
    
# Test function
def test():
    sol = Solution()

    test_cases = [
        ([1, 1, 1], 2, 2),  # Subarrays: [1,1], [1,1]
        ([1, 2, 3], 3, 2),  # Subarrays: [1,2], [3]
        ([1, 1, 1, 1], 3, 2),  # Subarrays: [1,1,1], [1,1,1]
        ([1, 2, 3, 4], 5, 2),  # Subarrays: [2,3], [1,4]
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = sol.subarraySum(nums, k)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()