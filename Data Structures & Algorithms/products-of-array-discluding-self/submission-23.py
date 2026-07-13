class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_moltiplication_value = 1
        zero_counter = 0
        res = [0] * len(nums)

        for num in nums:
            if num:
                total_moltiplication_value *= num
            else:
                zero_counter += 1

        if zero_counter > 1:
            return res
        
        for i,num in enumerate(nums):
            if zero_counter and num == 0:
                res[i] = int(total_moltiplication_value)
            elif not zero_counter:
                res[i] = int(total_moltiplication_value/num)

        return res


         