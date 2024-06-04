class Solution:
    def longestPalindrome(self, s: str) -> int:
        #two sol hashmap and hashset same logic but time comp decreased in set
        set1=set()
        res=0

        for c in s:
            if c in set1:
                set1.remove(c)
                res+=2
            else:
                set1.add(c)
        if set1:
            return res+1
        else:
            return res
        
        