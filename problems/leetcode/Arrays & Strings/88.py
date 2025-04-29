from typing import List

# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0
        r = m
        s = 0

        while s < len(nums2):
            if nums1[l] == 0:
                nums1[l] = nums2[s]
                l += 1
                r += 1
                s += 1
                continue

            if nums1[l] <= nums2[s]:
                l += 1
                continue

            nums1[r] = nums2[s]
            nums1[l], nums1[r] = nums1[r], nums1[l]
            r += 1
            s += 1
            l += 1
        
        print(nums1)


# Test function
def test():
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]

    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases):
        sol.merge(nums1, m, nums2, n)
        print(f"Test case {i + 1}: {'✅' if nums1 == expected else '❌'} | Output: {nums1} | Expected: {expected}")

if __name__ == "__main__":
    test()