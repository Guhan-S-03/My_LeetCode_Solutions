class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls=0
        rs=sum(nums)
        for ind,val in enumerate(nums):
            rs-=val
            if(rs==ls):
                return ind
            ls+=val
        return -1
        