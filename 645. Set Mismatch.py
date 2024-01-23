class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        l1=[0,0]
        for i in range(1,len(nums)+1):
            if(count[i]==0):
                l1[1]=i
            if(count[i]==2):
                l1[0]=i
        return l1


        