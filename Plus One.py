class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        largeint=0
        val=0
        for i in digits:
            val=val*10+i
        val+=1
        sval=str(val)
        list1=[]
        for i in sval:
            list1.append(int(i))
        return list1
