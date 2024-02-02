class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        sequence="123456789"
        lw=len(str(low))
        hw=len(str(high))
        for i in range(lw,hw+1):
            for j in range(0,10-i):
                num=int(sequence[j:j+i])
                if(num>=low and num<=high):
                    res.append(num)
        return res

        