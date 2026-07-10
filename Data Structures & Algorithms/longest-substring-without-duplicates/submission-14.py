class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        res = 0
        seen_chars_set = set()
        l = 0

        for i,c in enumerate(s):
            r = i
            if c in seen_chars_set:
                while l <= r and c in seen_chars_set:
                    seen_chars_set.remove(s[l])
                    l += 1
            else:
                res = max(res, r-l+1)
            seen_chars_set.add(c)
            
        return res
