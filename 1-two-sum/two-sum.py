class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            other=target-nums[i]
            if(hm.get(other,-1)==-1):
                hm[nums[i]]=i
            else:
                res=[-1,-1]
                res[0]=i
                res[1]=hm.get(other,-1)            
                return res
 
        