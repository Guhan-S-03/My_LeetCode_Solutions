class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #at every time we need a min possibble cookie than can satisfy that 
        #particular children becoz we can save the larger one for the child which has 
        #greed higher than this

        g.sort()
        s.sort()
        i,j=0,0

        while i<len(g):
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j<len(s):
                i+=1
                j+=1
            else:
                break
        return i        