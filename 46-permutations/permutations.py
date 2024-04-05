class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #recursive solution...everytime we pop the first element and precess other later we append that again and we do this for 
        #intial len of the array so eventually we ended upin permutaions
        result=[]

        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            lm=nums.pop(0)
            perms=self.permute(nums)

            for perm in perms:
                perm.append(lm)
            result.extend(perms)
            nums.append(lm)
        return result
                
