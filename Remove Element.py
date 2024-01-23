class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp=[]
        n=len(nums)
        for i in nums:
            if(i!=val):
                temp.append(i)
        k=len(temp)
        for j in range(n):
            if(j<k):
                nums[j]=temp[j]
            else:
                nums[j]='_'
        return k
