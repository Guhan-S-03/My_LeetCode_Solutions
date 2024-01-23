class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        scol=s[0]
        scol=alp.index(scol)
        ecol=s[3]
        ecol=alp.index(ecol)
        srow=int(s[1])
        erow=int(s[4])
        res=[]
        for col in range(scol,ecol+1):
            for row in range(srow,erow+1):
                cell=alp[col]
                cell+=str(row)
                res.append(cell)
        return res
        