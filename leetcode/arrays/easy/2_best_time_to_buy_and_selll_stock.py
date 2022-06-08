"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class BruteForceSolution:
    """Brute force solution

    * O(n) time complexity
    * O(1) space complexity
    """

    def max_profit(self, prices):
        length = len(prices)
        max_profit = 0
        min_price = prices[0]
        for i in range(1, length):
            if prices[i] < min_price:
                min_price = prices[i]
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    obj = BruteForceSolution()
    print(obj.max_profit(prices))
