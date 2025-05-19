from typing import List
# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
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
        ([8860, -853, 6534, 4477, -4589, 8646, -6155, -5577, -1656, -5779, -2619, -8604, -1358, -8009, 4983, 7063, 3104, 
        -1560, 4080, 2763, 5616, -2375, 2848, 1394, -7173, -5225, -8244, -809, 8025, -4072, -4391, -9579, 1407, 6700, 2421,
        -6685, 5481, -1732, -8892, -6645, 3077, 3287, -4149, 8701, -4393, -9070, -1777, 2237, -3253, -506, -4931, -7366, 
        -8132, 5406, -6300, -275, -1908, 67, 3569, 1433, -7262, -437, 8303, 4498, -379, 3054, -6285, 4203, 6908, 4433, 3077,
        2288, 9733, -8067, 3007, 9725, 9669, 1362, -2561, -4225, 5442, -9006, -429, 160, -9234, -4444, 3586, -5711, -9506,
        -79, -4418, -4348, -5891], 93, -594.5806451612904)  # A testcase with a large array from leetcode

    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = sol.findMaxAverage(nums, k)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()