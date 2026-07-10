class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter_s1 = [0]*26
        counter_substring_s2 = [0]*26

        for c1 in s1:
            counter_s1[ord(c1)-ord('a')]+=1
        
        for i in range(len(s1)):
            counter_substring_s2[ord(s2[i])-ord('a')] += 1
        l,r = 0,len(s1)
        # sliding window, update counter_substring_s2
        for i in range(len(s1),len(s2)):
            if counter_s1 == counter_substring_s2:
                return True
            r = i
            counter_substring_s2[ord(s2[l])-ord('a')] -= 1
            l += 1
            counter_substring_s2[ord(s2[r])-ord('a')] += 1


        return counter_s1 == counter_substring_s2