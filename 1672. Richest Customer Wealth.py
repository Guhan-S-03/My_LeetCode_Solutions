class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highw=0
        for listt in accounts:
            tot=sum(listt)
            highw=max(tot,highw)
        return highw
        