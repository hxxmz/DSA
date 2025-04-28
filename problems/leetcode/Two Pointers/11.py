# 11. Container With Most Water
from typing import List

def maxArea(height: List[int]) -> int:
    max_area = float('-inf')
    l, r = 0, len(height) - 1
    while l < r:
        current_area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, current_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area

print(maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(maxArea(height = [1,1]))
