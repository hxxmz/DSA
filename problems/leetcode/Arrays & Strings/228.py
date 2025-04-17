def summaryRanges(nums):

    if not nums: return []

    if len(nums) == 1:
        return [str(nums[0])]

    start = str(nums[0])

    result = []
    
    for i in range(1,len(nums)):
        if nums[i] - nums[i-1] == 1:
            continue

        if start != str(nums[i-1]):
            start += "->" + str(nums[i-1])

        result.append(start)
        start = str(nums[i])
    
    if start != str(nums[i]):
            start += "->" + str(nums[i])

    result.append(start)

    return result


print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))

print(summaryRanges([]))  # → []
print(summaryRanges([5]))  # → ['5']
print(summaryRanges([1,2,3,4]))  # → ['1->4']
print(summaryRanges([1,3,5,7]))  # → ['1', '3', '5', '7']
