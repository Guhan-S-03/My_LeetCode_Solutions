class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=[]
        n=len(nums)
        for i in nums:
            if(i not in temp):
                temp.append(i)
        k=len(temp)
        for j in range(n):
            if(j<k):
                nums[j]=temp[j]
            else:
                nums[j]='_'
        return k