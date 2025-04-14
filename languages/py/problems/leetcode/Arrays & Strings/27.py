def removeElement(nums, val: int) -> int:
    l = 0
    r = 0

    while r < len(nums):
        if nums[r] == val:
            nums[r] = val# "_"
            r += 1
            continue

        if l != r:
            nums[l] = nums[r]
            nums[r] = val# "_"

        l += 1
        r += 1

    return l

def removeElementOppositeEnds(nums, val: int) -> int:
    l = 0
    r = len(nums)-1

    while l <= r:
        if nums[r] == val:
            r -= 1
            continue
        if nums[l] == val:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        l += 1

    return l

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))
print(removeElement([2,3,2], 3))
print()
print(removeElementOppositeEnds([3,2,2,3], 3))
print(removeElementOppositeEnds([0,1,2,2,3,0,4,2], 2))
print(removeElementOppositeEnds([2,3,2], 3))