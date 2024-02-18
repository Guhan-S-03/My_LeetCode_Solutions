class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        dp=set()
        target=sum(nums)//2
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            temp=set()
            for val in dp:
                if(nums[i]+val)==target:
                    return True
                temp.add(nums[i]+val)
                temp.add(val)
            dp=temp
        return False

        
        