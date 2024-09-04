class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ##this is a mathematical one here we dont want to loop through
        #the range instead we can find the common prefix of outer range
        #by right shift them and after that again left shift that common prefix 
        #for no of times u actually right shifted and thats the result 
        #key here is two num have common prefix (from MSB)at that time we have "same values" 
        cnt=0
        while left!=right:
            left=left>>1
            right=right>>1
            cnt+=1
        return left<<cnt