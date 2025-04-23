def removeDuplicates(nums) -> int:
    l = 2
    for r in range(2, len(nums)):
        if nums[r] != nums[l-2]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    print(nums)
    return l

print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))
