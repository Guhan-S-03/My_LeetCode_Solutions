class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,cols=len(matrix),len(matrix[0])
        ##every time this row and its col getting changed
        #so we dont need to touch that for that j starts after that
        tmat=[[0 for i in range(rows)] for j in range(cols)]

        for i in range(rows):
            for j in range(cols):
                tmat[j][i]=matrix[i][j]
        return tmat
        