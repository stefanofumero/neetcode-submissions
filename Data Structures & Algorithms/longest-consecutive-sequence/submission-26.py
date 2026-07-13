class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        element_set = set(nums)
        res = 0

        for num in nums:
            cnt = 1
            while (num - cnt) in element_set:
                cnt += 1
            res = max(res,cnt)

        return res