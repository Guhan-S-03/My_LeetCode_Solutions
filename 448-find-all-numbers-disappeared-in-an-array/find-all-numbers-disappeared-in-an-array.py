class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #without using any memory like dict or set we are doing inplace to find missing values
        for n in nums:
            ind=abs(n)-1
            nums[ind]= -1*abs(nums[ind])
        res=[]
        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)
        return res


        