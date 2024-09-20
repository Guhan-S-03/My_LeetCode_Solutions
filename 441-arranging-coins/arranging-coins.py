class Solution:
    def arrangeCoins(self, n: int) -> int:
        stair=1
        while n>=stair:
            n-=stair
            stair+=1
        return stair-1

        


        