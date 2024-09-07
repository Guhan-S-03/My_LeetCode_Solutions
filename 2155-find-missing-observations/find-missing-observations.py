class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ##greedy way to split the values here that is
        #min(MAX_VALUE,cur_sum-remaining_pos+1)

        m=len(rolls)
        tot=mean*(n+m)

        remaining_sum=tot-sum(rolls)
        ##validate whether we can spit this sum into n parts on both extremes
        if remaining_sum>6*n or remaining_sum<n:
            return []
        
        res=[]
        while n:
            posible_val=min(6,remaining_sum-n+1)
            res.append(posible_val)
            remaining_sum-=posible_val
            n-=1
        return res

        