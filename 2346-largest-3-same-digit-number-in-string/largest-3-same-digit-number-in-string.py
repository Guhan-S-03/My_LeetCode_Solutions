class Solution:
    def largestGoodInteger(self, num: str) -> str:
        #we can do this in n time cmp
        #0 is smaller than 000 in string so we can utilize that
        res="0"

        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                res=max(res,num[i:i+3])
        return "" if res=="0" else res

        