class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ##here in this problem simultaneously the fruits are going to be rotten 
        #so we can maintain a queue to store the rotten fruits and its adjacent
        #that is going to rotten and also with the intial fresh count we can decide 
        #whether all the oranges are rotten are not

        rows,cols=len(grid),len(grid[0])
        q=deque()
        fresh=0
        time=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                row,col=q.popleft()
                for dr,dc in dir:
                    newr,newc=dr+row,dc+col
                    if (newr<0 or newr==rows or newc<0 or newc==cols or grid[newr][newc]!=1):
                        continue
                    grid[newr][newc]=2
                    fresh-=1
                    q.append([newr,newc])
            time+=1
        return time if fresh==0 else -1



        