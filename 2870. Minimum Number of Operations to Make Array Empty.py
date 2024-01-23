class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dict1=defaultdict(int) 
        for i in nums:
            dict1[i]+=1
        ans=0
        for i in dict1.values():
            if(i==1):
                return -1
            ans+=(i+2)//3
        return ans
           

        
        