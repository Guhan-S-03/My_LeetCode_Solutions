class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        mid=len(nums3)//2
        if(len(nums3)%2!=0):
            return float(nums3[mid])
        else:
            return ((nums3[mid]+nums3[mid-1])/2)

        