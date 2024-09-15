class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ##bit mask is used here to represent the state of prefix that we can remove to make the
        #substring that ends at that index so that we will have longest substring with even vowels
        #we are using the first 5 bits to represent the vowels from right

        vowels={
            'a':1,
            'e':2,
            'i':4,
            'o':8,
            'u':16
        }

        mask=0
        res=0
        masktoind=[-1]*32

        for i,c in enumerate(s):
            mask=mask ^ (vowels.get(c,0))
            if masktoind[mask]!=-1 or mask==0:
                lenn=i-masktoind[mask]
                res=max(res,lenn)
            else:
                masktoind[mask]=i
        return res

        