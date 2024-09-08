class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ##since k>=i and k<=j we can start from k and expand our subarray greedyly
        res=nums[k]
        l,r=k,k
        minn=nums[k]

        while l>0 or r<len(nums)-1:
            left=nums[l-1] if l>0 else 0
            right=nums[r+1] if r<len(nums)-1 else 0

            if left>right:
                l-=1
                minn=min(minn,left)
            else:
                r+=1
                minn=min(minn,right)
            res=max(res,(minn)*(r-l+1))
        return res
        