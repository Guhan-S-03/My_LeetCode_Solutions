class DetectSquares:

    def __init__(self):
        self.pts=[]
        self.freq=defaultdict(int)
    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.freq[tuple(point)]+=1
    def count(self, point: List[int]) -> int:
        px,py=point
        res=0
        for x,y in self.pts:
            if (abs(px-x)!=abs(py-y)) or px==x or py==y:
                continue
            res+=(self.freq[(x,py)]*self.freq[(px,y)])
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)