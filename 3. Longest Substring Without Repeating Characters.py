class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
        if(len(s)==1):
            return 1
        for i in range(len(s)-1):
            temp=[]
            temp.append(s[i])
            for j in range(i+1,len(s)):
                if(s[j] not in temp):
                    temp.append(s[j])
                else:
                    break
            lenn=len(temp)
            maxl=max(maxl,lenn)
        return maxl
        