class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        top=0
        bot=rows-1

        while top<=bot:
            mid=(top+bot)//2
            if target>matrix[mid][-1]:
                top=mid+1
            elif target<matrix[mid][0]:
                bot=mid-1
            else:
                break
        if not top<=bot:
            return False
        
        trow=(top+bot)//2

        l=0
        r=cols-1

        while l<=r:
            mid=(l+r)//2
            if target>matrix[trow][mid]:
                l=mid+1
            elif target<matrix[trow][mid]:
                r=mid-1
            else:
                return True
        return False
