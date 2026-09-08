class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        counter_s1 = [0] * 26
        counter_s2 = [0] * 26

        for i in range(n1):
            counter_s1[ord(s1[i]) - ord('a')] += 1
            counter_s2[ord(s2[i]) - ord('a')] += 1

        for r in range(n1, n2):
            if counter_s1 == counter_s2:
                return True
            
            counter_s2[ord(s2[r]) - ord('a')] += 1
            counter_s2[ord(s2[r - n1]) - ord('a')] -= 1

        return counter_s1 == counter_s2