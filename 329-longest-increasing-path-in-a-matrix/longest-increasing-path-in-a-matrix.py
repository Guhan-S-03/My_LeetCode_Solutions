class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #simply dfs for four possible condition and store the result in dp so that repeated work is avoided for further iterations
        rows,cols=len(matrix),len(matrix[0])
        dp={}#(r,c)

        def dfs(r,c,prevval):
            if(r<0 or r==rows or c<0 or c==cols or matrix[r][c]<=prevval):
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            res=1
            res=max(res,1+dfs(r+1,c,matrix[r][c]))
            res=max(res,1+dfs(r-1,c,matrix[r][c]))
            res=max(res,1+dfs(r,c+1,matrix[r][c]))
            res=max(res,1+dfs(r,c-1,matrix[r][c]))
            dp[(r,c)]=res
            return res
        maxx=-1
        for i in range(rows):
            for j in range(cols):
                maxx=max(maxx,dfs(i,j,-1))
        return maxx 
        