class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        prev = prices[0]

        for price in prices[1:]:
            if price>prev:
                max_profit += price-prev
            prev = price
        return max_profit