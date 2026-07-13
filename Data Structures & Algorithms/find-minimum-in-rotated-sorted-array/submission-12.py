class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums) - 1

        while l < r:
            m = (l+r)//2
            # you have divided the array in two halves
            # in order to find the min, you have to stay in the unsorted
            # half, if present, otherwise, if both are sorted, the result
            # is nums[l]
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]