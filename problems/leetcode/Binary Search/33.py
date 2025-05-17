from typing import List

# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1: return 0 if nums[0] == target else -1
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            pass
        return -1
    
    def search_oldApproach(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1: return 0 if nums[0] == target else -1
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if (m != n-1) and (nums[m + 1] < nums[m]): # we're at largest number (m+1 being minimum)
                if (target > nums[l]) and (target < nums[m]): # check if the target is on the left side
                    r = m - 1
                else: # move towards right side
                    l = m + 1
            elif (m != 0) and nums[m - 1] > nums[m]: # we're at minimum (m-1 being largest)
                if (target < nums[r]) and (target > nums[m]): # check if the target is on the right side
                    l = m + 1
                else:
                    r = m - 1
            elif target < nums[m]: # we're in a sorted array (or a part of it) which is not rotated (or affected by it)
                r = m - 1
            else:
                l = m + 1
        return -1

# Test Function
def test():
    sol = Solution()
    
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),       # Target exists at index 4
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),      # Target does not exist
        ([1], 0, -1),                        # Single element, target absent
        ([1], 1, 0),                         # Single element, target present
        ([3, 1], 1, 1),                      # Small rotated array, target present
        ([3, 1], 2, -1),                     # Small rotated array, target absent
        ([5, 6, 7, 8, 9, 1, 2, 3], 3, 7),    # Target at the end of rotated array
        ([5, 6, 7, 8, 9, 1, 2, 3], 5, 0),    # Target at the beginning of rotated array
        ([2, 3, 4, 5, 6, 7, 8, 1], 8, 6),    # Target at the end before rotation point
        ([1, 2, 3, 4, 5], 4, 3),             # No rotation, normal binary search
        ([1, 2, 3, 4, 5], 6, -1),            # No rotation, target absent
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.search(nums, target)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()