class Solution:
    def addDigits(self, num: int) -> int:
        ##the key idea here is when the num becomes single dig 
        #we can return ..so we can do this recursively or we can explicitly use stack 
        #here i am doing recursive one

        if num <=9:
            return num

        tot=0
        while num>0:
            rem=num%10
            num=num//10
            tot+=rem
        return self.addDigits(tot)
        