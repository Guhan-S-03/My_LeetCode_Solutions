class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ##so here we are using the union find to check whether these two nodes in the edges 
        #are already have a path or not ...if it is then it will create a cycle so we return that edge

        par=[p for p in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)

        def find(n):
            p=par[n]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p  

        def union(n1,n2):
            p1,p2=find(n1),find(n2)

            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True

        for e1,e2 in edges:
            if not union(e1,e2):
                return [e1,e2]