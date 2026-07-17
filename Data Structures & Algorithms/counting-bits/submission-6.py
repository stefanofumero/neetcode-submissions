class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Remember to report, in your notes, that, when transforming an int
        into its binary representation, you're dividing by 2 till 0, 
        time complexity = log(n)
        """
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp