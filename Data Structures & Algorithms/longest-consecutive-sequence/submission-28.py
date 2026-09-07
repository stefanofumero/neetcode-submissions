class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in nums:
            if num + 1 not in num_set:
                cnt = 1
                while num - cnt in num_set:
                    cnt += 1
                res = max(res,cnt)

        return res