class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            # recurr with the same index,giving the possibility to reuse it
            dfs(i, cur, total + nums[i])
            cur.pop()
            # Now, once backtracked, you can increase the index
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res