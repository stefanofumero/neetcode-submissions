class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            If you want to avoid the division, you have to think about the
            fact that each res is given by the mult by everything on the
            right and everything of the left
        """

        res = [1] * len(nums)
        tot_molt = 1

        for i in range(1,len(nums)):
            tot_molt *= nums[i-1]
            res[i] = tot_molt
        tot_molt = 1
        for i in range(len(nums)-2,-1,-1):
            tot_molt *= nums[i+1]
            res[i] *= tot_molt
        
        return res

         