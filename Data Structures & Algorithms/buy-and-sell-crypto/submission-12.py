class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for i in range(1,len(prices)):
            price = prices[i]
            if price < buy:
                buy = price
            else:
                res = max(res,price-buy)
        
        return res
