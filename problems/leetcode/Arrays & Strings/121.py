def maxProfit(prices) -> int:
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

print(maxProfit(prices = [7,1,5,3,6,4]))
print(maxProfit(prices = [1,2,3,4,5]))
print(maxProfit(prices = [7,6,4,3,1]))