from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums) -1

        for i,val in enumerate(nums):
            if val > 0:
                break

            if(i > 0 and val == nums[i-1]):
                continue
            
            l,r = i+1, n

            while l < r:
                total_sum = val + nums[l] + nums[r]
                if total_sum == 0:
                    res.append([val,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif total_sum < 0:
                    l += 1
                else:
                    r -= 1

        return res