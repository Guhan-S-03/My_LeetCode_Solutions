class Solution:
    def minOperations(self, s: str) -> int:
        #there are 2 possibilities only starts with 0 or 1
        #chk the both conditions and take the min changes needed

        ##checking the 010101
        startszero=0
        for i in range(len(s)):
            if i%2==0 and s[i]!='0':
                startszero+=1
            elif i%2!=0 and s[i]!='1':
                startszero+=1 
        ##checking the 101010
        startsone=0
        for i in range(len(s)):
            if i%2==0 and s[i]!='1':
                startsone+=1
            elif i%2!=0 and s[i]!='0':
                startsone+=1
        return min(startsone,startszero)
            

        