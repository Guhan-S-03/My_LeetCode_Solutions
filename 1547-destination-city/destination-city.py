class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #we want a dest that doesnt came as starting
        #so we can store all startings and chk the dest whether it is start
        #if not that is the sol

        starts=set()
        
        for p in paths:
            starts.add(p[0])
        
        for p in paths:
            if p[1] not in starts:
                return p[1]
        

            
        