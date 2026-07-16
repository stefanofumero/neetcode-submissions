class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        The solution here is to transform the number in base 10 into a number
        in base 2
        """
        counter = 0
        while n:
            if n%2 != 0:
                counter += 1
            n //= 2
        return counter