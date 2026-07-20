class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        Each element of the array may increase or decrease the sum. 
        When the value of the current subarray becomes negative or equal zero, it
        doesn't make sense to consider it.

        We can use a left and right pointer to keep track of the current sol
        """
        best_l,best_r = 0,0
        l,r = 0,0
        best_sum = -1
        current = 0

        for i,n in enumerate(nums):
            if not current:
                l = r = 1
            
            current += n
            if current >= 0:
                r+=1
                if current >= best_sum:
                    best_sum = current
                    best_l,best_r = l,r
            else:
                current = 0

        return best_sum if best_sum >= 0 else -1