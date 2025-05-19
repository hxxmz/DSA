from typing import List
# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pass
        summ = 0
        for i in range(k):
            summ += nums[i]
        max_sum = summ
        
        l = 0
        r = l + k
        while r < len(nums):
            summ -= nums[l]
            summ += nums[r]
            max_sum = max(max_sum, summ)
            l += 1
            r += 1
        
        return max_sum / k

# Test Function
def test():
    sol = Solution()
    
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),     # Subarray [12, -5, -6, 50] has the max average of 12.75
        ([5], 1, 5.0),                          # Single element, max average is the element itself
        ([0, 4, 0, 3, 2], 1, 4.0),              # Max single-element average is 4
        ([4, 2, 1, 3, 5], 2, 4.0),              # Subarray [3, 5] gives the max average of 4.0
        ([7, 8, 9, 1, 2, 3], 3, 8.0),           # Subarray [7, 8, 9] has the max average of 8.0
        ([100, 200, 300, 400], 2, 350.0),       # Subarray [300, 400] gives the max average of 350.0
        ([-1, -2, -3, -4], 2, -1.5),            # Subarray [-1, -2] has the max average of -1.5
        ([1, 1, 1, 1, 1], 5, 1.0),              # All elements are the same, average is just the element
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = sol.findMaxAverage(nums, k)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()