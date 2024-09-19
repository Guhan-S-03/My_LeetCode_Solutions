class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ##this is similar to the previous one that is the cs1
        #but the only difference here is we need to find the order in which the courses are 
        #taken so that every time we found that we can complete the particular course by completing
        #its prereq we append it to the output

        prereq={c:[] for c in range(numCourses)}
        for c,p in prerequisites:
            prereq[c].append(p)

        output=[]
        visit,cyc=set(),set()##these sets are to maintain current path and final completed one
        def dfs(crs):
            if crs in cyc:
                return False
            if crs in visit:
                return True
            cyc.add(crs)

            for preq in prereq[crs]:
                if not dfs(preq):
                    return False
            cyc.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return[]
        return output

        
        