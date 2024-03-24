class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prevdp=[0]*(amount+1)
        prevdp[0]=1

        for i in range(len(coins)-1,-1,-1):
            newdp=[0]*(amount+1)
            newdp[0]=1
            for j in range(1,amount+1):
                newdp[j]=prevdp[j]
                if j-coins[i]>=0:
                    newdp[j]+=newdp[j-coins[i]]
            prevdp=newdp
        return prevdp[amount]

        