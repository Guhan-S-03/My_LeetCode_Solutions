class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #bottom up
        rows,cols=len(grid),len(grid[0])
        dp=[[0]*cols for _ in range(cols)]

        for r in reversed(range(rows)):
            curdp=[[0]*cols for _ in range(cols)]
            #upper  traingle
            for c1 in range(cols-1):
                for c2 in range(c1+1,cols):
                    maxcherry=0
                    cherry=grid[r][c1]+grid[r][c2]
                    for c1d,c2d in product([-1,0,1], [-1,0,1]):
                        nc1,nc2=c1+c1d,c2+c2d
                        if nc1<0 or nc2==cols:
                            continue
                        maxcherry=max(maxcherry,cherry+dp[nc1][nc2])
                    curdp[c1][c2]=maxcherry
            dp=curdp
        return dp[0][cols-1]
        