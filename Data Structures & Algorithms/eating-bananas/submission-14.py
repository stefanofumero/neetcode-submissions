class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k is a value between 1 and max(piles)
        l,r = 1,max(piles)
        res = max(piles)

        def test_k(k:int):
            cnt = 0
            for p in piles:
                cnt += math.ceil(p/k)
            return cnt

        while l <= r:
            m = (l+r)//2
            cnt = test_k(m)
            if cnt <= h:
                res = min(res,m)
                r = m-1
            else:
                l = m+1


        return res