class Solution:
    def validPalindrome(self, s: str) -> bool:
        #usual l,r technique

        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                #in that case we need to chk whether palindrome exist 
                #if we remove any one char
                skipl=s[l+1:r+1]
                skipr=s[l:r]
                return (skipl==skipl[::-1] or skipr==skipr[::-1])
            l+=1
            r-=1
        return True
        