def findClosestNumber(nums) -> int:
    minimum_value = nums[0]
    minimum_difference = abs(nums[0])
    for current_value in nums:
        if abs(current_value) < minimum_difference:
            minimum_value = current_value
            minimum_difference = abs(current_value)
        elif (abs(current_value) == minimum_difference) and (current_value > minimum_value):
            minimum_value = current_value
    return minimum_value

print(findClosestNumber([2,-1,1]))
print(findClosestNumber([-4,-2,1,4,8]))
