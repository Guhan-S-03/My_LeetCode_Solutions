class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ind=nums[i]
            val=nums[ind]
            ans.append(val)
        return ans
        