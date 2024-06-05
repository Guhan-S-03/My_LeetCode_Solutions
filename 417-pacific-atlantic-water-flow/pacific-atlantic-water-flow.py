class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #actually we are working in a backward manner that is from ocean end to inwards
        #from four end we are finding the incr node that can reach that end with two sets
        #and comparing that twosets to find intersecting cell that can reach both oceans

        rows,cols=len(heights),len(heights[0])
        pac,atl=set(),set()

        def dfs(r,c,visit,prevh):
            if(r<0 or c<0 or r==rows or c==cols or
            heights[r][c]<prevh or (r,c)in visit):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res