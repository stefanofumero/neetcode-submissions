class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            you know the target upfront, meaning that, for each value in the array:
            missing = target - num. If already met missing
        """
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i