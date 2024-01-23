class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        while(len(nums)>0):
            al=nums.pop(0)
            bob=nums.pop(0)
            arr.append(bob)
            arr.append(al)
        return arr

        