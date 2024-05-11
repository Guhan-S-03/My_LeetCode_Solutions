class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]

        for i in range(len(nums1)):
            val=nums1[i]
            j=nums2.index(val)
            flag=0
            for newj in range(j+1,len(nums2)):
                if nums2[newj]>val:
                    flag=1
                    ans.append(nums2[newj])
                    break
            if not flag:
                ans.append(-1)
        return ans
        