class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp=max(nums)
        maxs,mins=1,1
        for i in nums:
            if i == 0:
                maxs,mins=1,1
                continue
            temp = maxs*i
            maxs = max(maxs*i,i*mins,i)
            mins = min(temp,i*mins,i)
            maxp=max(maxp,maxs)
        return maxp
            

        