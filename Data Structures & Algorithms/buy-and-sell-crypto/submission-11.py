class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # One single price: no sense to sell or buy
        if len(prices) == 1:
            return 0
        
        res = 0
        l, r = prices[0],prices[1]

        for i in range(1,len(prices)):
            r = prices[i]
            res = max(res, r - l)
            if r <= l:
                l = r

        return res