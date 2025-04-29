from typing import List

# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length

        # calculate the accumulative product from the left and right of the each index  
        prefix_products = [0] * length
        product = 1
        for i in range(length):
            prefix_products[i] = product
            product *= nums[i]
        # print(prefix_products)

        product = 1
        suffix_products = [0] * length
        for i in range(length-1, -1, -1):
            suffix_products[i] = product
            product *= nums[i]
        # print(suffix_products)

        # product of current index is the product of sub arrays left and right to it
        for i in range(length):
            answer[i] = prefix_products[i] * suffix_products[i]

        return answer

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.productExceptSelf(nums)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()