def removeDuplicates(nums) -> int: # dry approach
    l = 0
    r = 1

    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]

        nums[r] = "_"
        r += 1

    print(nums)
    return l+1

def removeDuplicatesTwo(nums) -> int: # first approach
    l = 0
    r = 1

    while r < len(nums):
        if nums[l] == nums[r]:
            nums[r] = "_"
            r += 1
            continue
        l += 1
        nums[l] = nums[r]
        nums[r] = "_"
        r += 1

    print(nums)
    return l+1


print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([]))
