class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #similar to the no of island prob
        #but here we actually count the max area of the island
        #we can do that by adding 1 to the cur area if it is a proper land(not visited)
        #else return 0
        rows,cols=len(grid),len(grid[0])
        visited=set()

        def dfs(r,c):
            if(r<0 or r==rows or c<0 or c==cols or 
            grid[r][c]==0 or (r,c) in visited):
                return 0
            
            visited.add((r,c))
            return (1+dfs(r+1,c)+
            dfs(r-1,c)
            +dfs(r,c+1)
            +dfs(r,c-1))
        maxa=0
        for r in range(rows):
            for c in range(cols):
                maxa=max(maxa,dfs(r,c))
        return maxa
        