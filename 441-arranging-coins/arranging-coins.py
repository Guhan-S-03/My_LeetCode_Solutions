class Solution:
    def arrangeCoins(self, n: int) -> int:
        ##so the simple iteration for every step also works and find the answer
        #but here we are using the guass formula to find the no of rows we can complete

        l,r=1,n
        res=0

        while l<=r:
            mid=(l+r)//2
            req_coins=(mid/2)*(mid+1)
            if req_coins>n:
                r=mid-1
            else:
                res=max(res,mid)
                l=mid+1
        return res 

        


        