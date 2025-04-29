from typing import List

# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # we follow the thought process similar to 3sum

        nums.sort()
        length = len(nums)
        closest_difference = float('inf')
        closest_sum = None
        for i in range(length):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = length - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                current_difference = abs(target - current_sum)

                # On exact match, return the sum
                if current_sum == target:
                    return current_sum
                
                # Update the closest sum if we find a smaller difference
                if current_difference < closest_difference:
                    closest_difference = current_difference
                    closest_sum = current_sum
                
                # Move the pointer according to where the sum lie
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return closest_sum

# Test function
def test():
    sol = Solution()
    
    test_cases = [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.threeSumClosest(nums, target)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()