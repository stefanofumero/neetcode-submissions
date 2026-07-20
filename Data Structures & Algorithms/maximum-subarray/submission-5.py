class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        Each element of the array may increase or decrease the sum. 
        When the value of the current subarray becomes negative or equal zero, it
        doesn't make sense to consider it.

        We can use a left and right pointer to keep track of the current sol
        """
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub