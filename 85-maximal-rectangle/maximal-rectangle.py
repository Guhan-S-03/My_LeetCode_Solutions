class Solution:
    def maxarea(self,height):
        maxa=0
        stack=[]
        for i,h in enumerate(height):
            start=i
            while stack and stack[-1][1]>h:
                ind,ht=stack.pop()
                maxa=max(maxa,ht*(i-ind))
                start=ind
            stack.append((start,h))
        for i,h in stack:
            maxa=max(maxa,h*(len(height)-i))
        return maxa
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        height=[0]*cols
        max_a=0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    height[c]+=1
                else:
                    height[c]=0
            max_a=max(max_a,self.maxarea(height))
        return max_a

                
            
        