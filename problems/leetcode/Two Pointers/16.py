# 16. 3Sum Closest
from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
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

            # exact match, return the sum
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

print(threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(threeSumClosest(nums = [0,0,0], target = 1))