# 1. Two Sum

def twoSum(nums, target: int):

    # Time: O(n)
    # Space: O(n)

    seen = {}
    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [seen[target - nums[i]], i]
        seen[nums[i]] = i

print(twoSum(nums = [2,7,11,15], target = 9)) # [0, 1]
print(twoSum(nums = [3,2,4], target = 6)) # [1, 2]
print(twoSum(nums = [3,3], target = 6)) # [0, 1]
print(twoSum(nums = [1, 2, 3, 4, 5], target = 9)) # [3, 4]