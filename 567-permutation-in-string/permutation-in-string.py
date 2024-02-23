class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        
        ls1=[0]*26
        ls2=[0]*26
        matches=0
        for i in range(len(s1)):
            ls1[ord(s1[i])-ord('a')]+=1
            ls2[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            if(ls1[i]==ls2[i]):
                matches+=1
        l=0

        for r in range(len(s1),len(s2)):
            if matches==26:
                return True

            index=ord(s2[r])-ord('a')
            ls2[index]+=1
            if(ls2[index]==ls1[index]):
                matches+=1
            elif(ls1[index]+1==ls2[index]):
                matches-=1
            index=ord(s2[l])-ord('a')
            ls2[index]-=1
            if(ls2[index]==ls1[index]):
                matches+=1
            elif(ls1[index]-1==ls2[index]):
                matches-=1
            l+=1
        return matches==26



