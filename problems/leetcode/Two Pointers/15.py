# 15. 3Sum
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # using built-in sort, not the main concern
    nums.sort()
    answer = []
    length = len(nums)
    # three indices i, j, k && a: nums[i], b: nums[j], c: nums[k]
    for i in range(length):
        j = i + 1
        k = length - 1
        while j < k:           
            # check if they sum to 0
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                # print(f"[{i}] a: {nums[i]} | [{j}] b: {nums[j]} | [{k}] c: {nums[k]}")
                answer.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
    return answer

print(threeSum(nums = [-1,0,1,2,-1,-4]))
print(threeSum(nums = [0,1,1]))
print(threeSum(nums = [0,0,0]))
