class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy,sell = 0,1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit,profit)
            else:
                buy = sell #we found a really low price so we want to buy that
            sell += 1
        return maxProfit 
                

        