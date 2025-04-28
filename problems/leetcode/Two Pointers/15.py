# 15. 3Sum
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
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

print(threeSum(nums = [-1,0,1,2,-1,-4]))
print(threeSum(nums = [0,1,1]))
print(threeSum(nums = [0,0,0]))
