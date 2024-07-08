class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows,cols=len(mat),len(mat[0])

        sum_diag=0
        for i in range(rows):
            sum_diag+=(mat[i][i])
            if i!=rows-1-i:
                sum_diag+=(mat[i][rows-1-i])
        return sum_diag
        
        