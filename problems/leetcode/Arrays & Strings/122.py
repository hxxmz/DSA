from typing import List

# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
            
        return profit

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 7), # Buy at 1, sell at 5, buy at 3, sell at 6
        ([1, 2, 3, 4, 5], 4), # Buy at 1, sell at 5
        ([7, 6, 4, 3, 1], 0), # No profit as prices are in decreasing order
    ]

    for i, (prices, expected) in enumerate(test_cases):
        result = sol.maxProfit(prices)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()