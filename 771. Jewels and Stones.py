class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        totj=0
        for i in stones:
            if(i in jewels):
                totj+=1
        return totj
        