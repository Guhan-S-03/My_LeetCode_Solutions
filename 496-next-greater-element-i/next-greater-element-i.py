class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #monotonic stack
        ind1={val:i for i,val in enumerate(nums1)}
        res=[-1]*len(nums1)

        stack=[]
        for j in range(len(nums2)):
            val=nums2[j]
            while stack and val>stack[-1]:
                pop=stack.pop()
                ind=ind1[pop]
                res[ind]=val
            if val in nums1:
                stack.append(val)
        return res

        