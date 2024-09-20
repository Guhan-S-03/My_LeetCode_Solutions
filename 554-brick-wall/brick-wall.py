class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ##so if have a total width of n and unit width is 1 then we have 
        #n-1 gaps(ends here) we dont want the extreme ends 
        #we want to find the gaps count in every row 
        #then we want the gap that had highest count because 
        #when we cut at that gap we will have min no of brick cut

        countgap={0:0}

        for r in wall:
            tot=0
            for b in r[:-1]:
                tot+=b
                countgap[tot]=1+countgap.get(tot,0)
        
        return len(wall)-max(countgap.values())

        