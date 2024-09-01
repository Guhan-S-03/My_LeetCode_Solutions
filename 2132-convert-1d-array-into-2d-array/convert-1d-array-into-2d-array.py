class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []

        res_mat=[[0 for j in range(n) ]for i in range(m)]
        k=0
        for i in range(m):
            for j in range(n):
                res_mat[i][j]=original[k]
                k+=1
        return res_mat


        