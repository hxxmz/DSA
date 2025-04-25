def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    colors = {}
    for color in nums:
        if color not in colors:
            colors[color] = 1
            continue
        colors[color] += 1
    
    current = 0
    for i in range(len(nums)):
        if colors[current] == 0:
            current += 1
        nums[i] = current
        colors[current] -= 1

    print(nums)

def DutchNationalFlagAlgorithm(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left, right = 0, len(nums)-1
    current = 0
    
    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left +=1
            current += 1
        elif nums[current] == 1:
            current += 1
        elif nums[current] == 2:
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1

    print(nums)

sortColors(nums = [2,0,2,1,1,0])
sortColors(nums = [2,0,1])

DutchNationalFlagAlgorithm(nums = [2,0,2,1,1,0])
DutchNationalFlagAlgorithm(nums = [2,0,1])