class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #checking whether cycle present or not if present return false
        #else satisfies each course by remov prereq and finally run dfs on every node and verify

        premap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visited=set()

        def dfs(crs):
            if(crs in visited):
                return False
            if premap[crs] == []:
                return True
            visited.add(crs)
            for preq in premap[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            premap[crs]=[]
            return True
        
        #becoz there may be chance that the given graph in not fully connected
        #like 1->2 and 3->4
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        