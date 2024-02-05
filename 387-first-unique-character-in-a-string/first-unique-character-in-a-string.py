class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = defaultdict(int)
        for char in s:
            dict1[char] += 1
        for i,char in enumerate(s):
            if(dict1[char]==1):
                return i
        return -1

        
