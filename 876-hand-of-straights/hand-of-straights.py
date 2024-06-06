class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # with the help of hashmap and minheap we can solve
        #every time we take min value and try to find consecutive elements
        hashmap={}
        for h in hand:
            hashmap[h]=1+hashmap.get(h,0)
        minh=list(hashmap.keys())
        heapq.heapify(minh)

        while minh:
            first=minh[0]
            for i in range(first,first+groupSize):
                if i not in hashmap:
                    return False
                hashmap[i]-=1
                if(hashmap[i]==0):
                    if(minh[0]!=i):
                        return False
                    heapq.heappop(minh)
        return True
                



        