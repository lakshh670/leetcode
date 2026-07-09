class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost_price,profit=prices[0],0
        n=len(prices)
        for i in range(n):
            if prices[i]>cost_price:
                profit=max(profit,prices[i]-cost_price)
            else:
                cost_price=prices[i]
        return profit