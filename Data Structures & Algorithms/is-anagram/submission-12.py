class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length is different, they cannot be anagrams
        if len(s) != len(t):
            return False

        counter_s,counter_t=[0]*26,[0]*26

        for char_s,char_t in zip(s,t):
            counter_s[ord(char_s)-ord('a')]+=1
            counter_t[ord(char_t)-ord('a')]+=1

        return counter_s == counter_t