class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = prices[0]

        for sell in prices:
            res = max(res, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return res