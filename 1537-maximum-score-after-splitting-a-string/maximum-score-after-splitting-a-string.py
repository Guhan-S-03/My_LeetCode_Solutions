class Solution:
    def maxScore(self, s: str) -> int:
        #calc the tot 1ss and each point from beg reduce 1 count and incr 0 count if present and
        #calculates max with these l and r values
        rones=0
        lzeros=0
        for v in s:
            if int(v):
                rones+=1

        maxs=0
        for i in range(len(s)-1):
            v=s[i]
            if int(v):
                rones-=1
                maxs=max(maxs,rones+lzeros)
            else:
                lzeros+=1
                maxs=max(maxs,rones+lzeros)
        return maxs
        