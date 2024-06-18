class Solution:
    def isPathCrossing(self, path: str) -> bool:
        #path crossed in the sense that point is visited twice
        hashmap={"N":[0,1],"S":[0,-1],"E":[1,0],"W":[-1,0]}
        x,y=0,0
        visited=set()

        for d in path:
            visited.add((x,y))
            nx,ny=hashmap[d]
            x,y=x+nx,y+ny
            if (x,y) in visited:
                return True
        return False

        