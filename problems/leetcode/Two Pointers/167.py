# 167. Two Sum II - Input Array Is Sorted
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:

    #Start from the beginning and end. 
    # if target < sum of two pointer values, r -= 1 (shrink the sum by lowering high value)
    # if target > sum then we need greater left value to level the sum
    # return index + 1 (1-indexed array of integers) of both values that add to the target
    # it is guaranteed that there's a result, "there is exactly one solution"

    length = len(numbers)
    l, r = 0, length - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target: # can be else just here for clarity
            l += 1
 
print(twoSum(numbers = [2,7,11,15], target = 9))
print(twoSum(numbers = [2,3,4], target = 6))
print(twoSum(numbers = [-1,0], target = -1))
