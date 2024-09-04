class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y=0,0
        res=0
        d=0
        ##the reason for this order is it resembles the actual dir "nesw"
        dirr=[[0,1],[1,0],[0,-1],[-1,0]]
        obs={tuple(v)for v in obstacles}
        for c in commands:
            if c== -1:
                d=(d+1)%4
            elif c==-2:
                d=(d-1)%4
            else:
                xx,yy=dirr[d]
                for m in range(c):
                    if (x+xx,y+yy) in obs:
                        break
                    x=x+xx
                    y=y+yy
                    res=max(res,x**2+y**2)
        return res


        