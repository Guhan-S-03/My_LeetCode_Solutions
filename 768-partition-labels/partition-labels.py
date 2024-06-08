class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #with the help of hashmap we can store the lastindex of the char
        #with that we can partion the array and store those size in to the res array
        hashmap={}
        for i,c in enumerate(s):
            hashmap[c]=i
        
        size=0
        end=0
        res=[]
        for i,c in enumerate(s):
            size+=1
            end=max(end,hashmap[c])
            if i==end:
                res.append(size)
                size=0
        return res
