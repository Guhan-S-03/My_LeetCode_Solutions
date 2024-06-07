class Solution:
    def jump(self, nums: List[int]) -> int:
        #actually we are doing bfs in 1d array with windows indicating
        #the no of jumps from that loc
        res=0
        l,r=0,0

        while  r<len(nums)-1:
            far=0
            for i in range(l,r+1):
                far=max(far,i+nums[i])
            l=r+1
            r=far
            res+=1
        return res
        