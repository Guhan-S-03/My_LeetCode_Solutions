class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #its a modification of no of components here it is cities and provinces 
        #union find alg to find no of components
        #we need intial no of comp and par and rank
        rows,cols=len(isConnected),len(isConnected)

        par=[i for i in range(rows)]
        rank=[1]*rows

        def findpar(n1):
            res=n1
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res

        def union(n1,n2):
            p1,p2=findpar(n1),findpar(n2)

            if p1==p2:
                return 0
            
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2]=p1
                rank[p1]+=rank[p2]
            return 1

        nofc=rows
        for i in range(rows):
            for j in range(i+1,rows):
                if isConnected[i][j]==1:
                    nofc-=union(i,j)
        return nofc
        