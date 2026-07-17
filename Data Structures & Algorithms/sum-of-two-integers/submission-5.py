class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            
            bit_res = bit_a ^ bit_b ^ carry
            carry = 1 if (bit_a + bit_b + carry) >= 2 else 0
            res += (bit_res << i)
        
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res