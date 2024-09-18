from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ##so the default sorting will not be suitable here
        #because here we need to arrange the element in a order such that
        #if we combine them we should get the largest num
        ##so a+b>b+a
        nums1=list(map(str,nums))
        def compare(x,y):
            if x+y>y+x:
                return -1
            else:
                return 1


        nums1.sort(key=cmp_to_key(compare))
        res="".join(nums1)
        return res if res[0]!='0' else '0'


        