class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ##we know that each diagonal cell index increases by 1 for both (r,c)
        #so using this we can move on for different diagonals and sort them update them
        #we can use a list and sort it and than we update the matrix using the sorted list but
        #here mat ele are from 1-100 so we can use counting sort
        rows,cols=len(mat),len(mat[0])

        def sortdiagonal(r,c):
            count=[0]*(101)
            rr=r
            cc=c
            while(r<rows and c<cols):
                count[mat[r][c]]+=1
                r+=1
                c+=1
            
            for i in range(1,101):
                while count[i]>0:
                    mat[rr][cc]=i
                    count[i]-=1
                    rr+=1
                    cc+=1

        for c in range(cols):
            sortdiagonal(0,c)
        
        for r in range(1,rows):
            sortdiagonal(r,0)
        
        return mat
        