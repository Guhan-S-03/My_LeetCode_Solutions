class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #like all the bt prob here also we do dfs with cleanup activity
        #here we use cols,posd,negd concepts to prevent the attcking of queens
        cols=set()
        posdiag=set()
        negdiag=set()
        res=[]
        board=[["."]*n for i in range(n)]

        def backtrack(r):
            if r==n:
                copyofboard=["".join(row)for row in board]
                res.append(copyofboard)
                return
            for c in range(n):
                if c in cols or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]="Q"

                backtrack(r+1)
                #chances that the prev cols that satisfied might be not satified on further proceedings
                #so we have to cleanup and try the next column
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res



        