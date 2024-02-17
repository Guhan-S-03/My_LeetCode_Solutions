class Solution:
    def longestPalindrome(self, s: str) -> str:
        largep=""
        for i in range(len(s)):
            odd1=self.largestpalindrome(s,i,i)
            even1=self.largestpalindrome(s,i,i+1)
            if len(odd1)>len(even1) and len(odd1)>len(largep):
                largep=odd1
            elif len(odd1)<len(even1) and len(even1)>len(largep) :
                largep=even1
            elif len(odd1)==len(even1) and len(odd1)>len(largep):
                largep=odd1
        return largep


    def largestpalindrome(self,s,l,r):
        largepalindrome=""
        while l>=0 and r<len(s) and s[l]==s[r]:
            largepalindrome=s[l:r+1]
            l-=1
            r+=1
        return largepalindrome

        