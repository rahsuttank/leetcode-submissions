class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        n = len(prices)
        sell = 0
        profit = 0
        while sell < len(prices):
            while sell + 1 < n and prices[sell + 1] > prices[sell]:
                sell += 1
            print(buy, sell)
            if sell < n:
                profit += (prices[sell] - prices[buy])
            buy = sell + 1
            sell = buy
        
        return profit
            

        