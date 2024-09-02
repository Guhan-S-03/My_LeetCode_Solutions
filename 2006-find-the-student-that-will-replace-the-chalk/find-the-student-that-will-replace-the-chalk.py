class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        ##the key here is to reduce the successful iterations from the given chalk
        #because we know that they can happen with the remaining ones we need to iterate and find the index
        #that lacks the chalk
        k=k%sum(chalk)
        
        for i in range(len(chalk)):
            if chalk[i]<=k:
                k=k-chalk[i]
            else:
                return i
        