from typing import List

# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
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

    def removeElementOppositeEnds(self, nums: List[int], val: int) -> int:
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

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([3, 2, 2, 3], 3, 2),  # Expected output: 2
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),  # Expected output: 5
        ([2, 3, 2], 3, 2)  # Expected output: 2
    ]

    print("Testing removeElement:")
    for i, (nums, val, expected) in enumerate(test_cases):
        result = sol.removeElement(nums, val)
        print(f"Test case {i + 1}:")
        print(f"  Output: {result} | Expected: {expected} {'✅' if result == expected else '❌'}")

    print("\nTesting removeElementOppositeEnds:")
    for i, (nums, val, expected) in enumerate(test_cases):
        result = sol.removeElementOppositeEnds(nums, val)
        print(f"Test case {i + 1}:")
        print(f"  Output: {result} | Expected: {expected} {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    test()