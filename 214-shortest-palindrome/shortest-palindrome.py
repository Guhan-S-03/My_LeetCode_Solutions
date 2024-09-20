class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ##just find the longest prefix palindrome and reverse the remaining thing
        #and prepend it to the s is the ans we can do it iteratively but thats n^2
        #so we can use some hashing technique to convert this string into the (base29)
        #representation so that we can compare the numbers in a constant time
        #and we can find the last part and reverse it
        ##we can use any base from 27 but taking prime is safe side
        
        prefix=0
        suffix=0
        lastindex=0
        base=29
        pos=1
        mod=10**9+7

        for i,c in enumerate(s):
            char=(ord(c)-ord('a'))+1
            prefix=(prefix*base)%mod
            prefix=(prefix+char)%mod
            suffix=(suffix+(char*pos))%mod
            pos=(pos*base)%mod
            if prefix==suffix:
                lastindex=i

        last=s[lastindex+1:]
        return last[::-1]+s



        
        

        