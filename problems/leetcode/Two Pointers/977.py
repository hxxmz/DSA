# 977. Squares of a Sorted Array
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:

    # initially i started with squaring the array in-place and then 
    # rearranging the values by swapping using two pointers
    # but a better approach would be to rearrange using two pointers 
    # and populating a resultant array in the required order, and perhaps squaring it while/before placing it.

    length = len(nums)
    l, r = 0, length - 1
    resultant_array = [None] * length
    resultant_arr_ptr = length - 1
    while l <= r:
        if abs(nums[l]) < abs(nums[r]):
            resultant_array[resultant_arr_ptr] = nums[r] ** 2
            r -= 1
        else:
            resultant_array[resultant_arr_ptr] = nums[l] ** 2
            l += 1
        resultant_arr_ptr -= 1

    return resultant_array

print(sortedSquares(nums = [-4,-1,0,3,10]))
print(sortedSquares(nums = [-7,-3,2,3,11]))
