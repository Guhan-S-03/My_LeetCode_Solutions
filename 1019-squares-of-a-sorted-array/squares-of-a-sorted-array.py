class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ##since neg ele also present here we r going to have 
        #2 pointers and build the squares in reverse order that is from higher 
        #to lower values -- we can build it in smaller to higher from middle
        l,r=0,len(nums)-1
        res=[]

        while l<=r:
            if nums[l]**2 > nums[r]**2:
                res.append(nums[l]**2)
                l+=1
            else:
                res.append(nums[r]**2)
                r-=1
        return res[::-1]
            

        