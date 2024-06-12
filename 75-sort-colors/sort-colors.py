class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap=defaultdict(int)#storing freq

        k=0
        for n in nums:
            hashmap[n]+=1
        for i in range(3):
            for j in range(hashmap[i]):
                nums[k]=i
                k+=1
        

        