class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ##just sort it so neg as well as pos are in their places
        #and also only 3 ele we need to choose so only 2 possiblities
        nums.sort()
        p1=nums[-1]*nums[-2]*nums[-3]
        p2=nums[0]*nums[1]*nums[-1]
        return max(p1,p2)

        