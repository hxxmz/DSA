from typing import List

# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum_seen = prices[0]

        for i in range(1, len(prices)):
            current_price = prices[i]
            if current_price < minimum_seen:
                minimum_seen = current_price

            current_profit = current_price - minimum_seen
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1 and sell at 6
        ([1, 2, 3, 4, 5], 4),      # Buy at 1 and sell at 5
        ([7, 6, 4, 3, 1], 0),      # No profit as prices are in decreasing order
    ]

    for i, (prices, expected) in enumerate(test_cases):
        result = sol.maxProfit(prices)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()