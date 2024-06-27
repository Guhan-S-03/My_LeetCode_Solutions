class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ##we can use a set to store the nodes and any node appears 
        #twice that will be the answer

        hashset=set()

        for e in edges:
            for n in e:
                if n in hashset:
                    return n
                else:
                    hashset.add(n)
              