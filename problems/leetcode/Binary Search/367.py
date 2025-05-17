# 367. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l <= r:
            m = (l + r) // 2
            sq = m * m
            if sq == num:
                return True
            elif sq > num:
                r = m - 1
            elif sq < num:
                l = m + 1
        return False

    def isPerfectSquare_unoptimized(self, num: int) -> bool:
        l = 1
        r = num
        while True:
            m = (l + r) / 2
            sq = m * m
            if sq == num:
                return True if (m % 1 == 0) else False
            elif sq > num:
                r = m - 1
            elif sq < num:
                l = m + 1

# Test Function
def test():
    sol = Solution()
    
    test_cases = [
        (16, True),       # 4 * 4 = 16
        (25, True),       # 5 * 5 = 25
        (1, True),        # 1 * 1 = 1
        (14, False),      # 14 is not a perfect square
        (100, True),      # 10 * 10 = 100
        (101, False),     # 101 is not a perfect square
        (2147395600, True),  # 46340 * 46340 = 2147395600 (maximum edge case)
        (2147483647, False), # Largest 32-bit signed integer
    ]

    for i, (num, expected) in enumerate(test_cases):
        result = sol.isPerfectSquare(num)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()