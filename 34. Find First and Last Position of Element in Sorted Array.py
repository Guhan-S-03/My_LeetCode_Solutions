class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target not in nums):
            arr=[-1,-1]
            return arr
        ind=[]
        findx=nums.index(target)
        lindx=len(nums)-nums[::-1].index(target)-1
        ind.append(findx)
        ind.append(lindx)
        return ind
        