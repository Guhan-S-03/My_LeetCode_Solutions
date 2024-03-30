class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #key note is we are not choosing element, poping tehm and check others we do the reverse we take a element and consider them as the 
        #last one poping and then found the what about the others
        nums=[1]+nums+[1]
        dp={}#(l,r)

        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)]=0
            for i in range(l,r+1):
                coins=nums[l-1]*nums[i]*nums[r+1]
                coins+=dfs(l,i-1)+dfs(i+1,r)
                dp[(l,r)]=max(dp[(l,r)],coins)
            return dp[(l,r)]
        return dfs(1,len(nums)-2)

        