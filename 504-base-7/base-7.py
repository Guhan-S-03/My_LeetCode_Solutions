class Solution:
    def convertToBase7(self, num: int) -> str:
        ##simply we need to divide it by 7 and form a string of the remainder
        if num==0:
            return "0"
        neg=False
        if num<0:
            neg=True
            num=abs(num)
        
        ans=""
        while num>0:
            rem=num%7
            num=num//7
            ans+=str(rem)
        if neg:
            return "-"+ans[::-1]
        else:
            return ans[::-1]

        