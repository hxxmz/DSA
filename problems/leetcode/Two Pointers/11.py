from typing import List

# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # start with pointers on each end
        # we calculate the area using min height of the two pointers times the distance between them
        # we keep track of the largest area that comes by
        # for movement of the pointers, the pointer of the smaller height is moved towards center;
        # retaining the max height for maximum potential area

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

# Test function
def test():
    sol = Solution()
    
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2)
    ]
    
    for i, (height, expected) in enumerate(test_cases):
        result = sol.maxArea(height)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()
