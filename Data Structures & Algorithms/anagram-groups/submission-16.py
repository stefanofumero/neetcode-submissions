class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We can create a dict, where the key is a counting array,
        # while the value is a list of elements (anagrams)
        listMap = defaultdict(list)

        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c)-ord('a')]+=1
            
            listMap[tuple(count)].append(str)

        return [l for l in listMap.values()]