# Author: Sakthi Santhosh
# Created on: 01/08/2023
#
# 121 - Best Time to Buy and Sell Stocks (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
def max_profit(prices: list[int]) -> int:
    profit_max = 0
    price_min = prices[0]

    for price in prices[1:]:
        if price < price_min:
            price_min = price
        else:
            profit_max = max(profit_max, price - price_min)
    return profit_max

if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))
