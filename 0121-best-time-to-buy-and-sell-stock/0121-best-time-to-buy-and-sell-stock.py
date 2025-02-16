class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        purchace_price = prices[0]
        for price in prices[1:]:
            if price < purchace_price:
                purchace_price = price
            else:
                profit = max(profit, price - purchace_price)
        return profit
        