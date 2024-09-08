class Solution:
    def totalNQueens(self, n: int) -> int:
        ##similar to the nqueen problem here we need only no of possibilities

        cols=set()
        posd=set()
        negd=set()
        res=0

        def backtrack(r):
            if r==n:
                nonlocal res
                res+=1
                return 
            
            for c in range(n):
                if c in cols or (r+c) in posd or (r-c) in negd:
                    continue
                
                cols.add(c)
                posd.add(r+c)
                negd.add(r-c)
                backtrack(r+1)

                cols.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
        backtrack(0)
        return res
        