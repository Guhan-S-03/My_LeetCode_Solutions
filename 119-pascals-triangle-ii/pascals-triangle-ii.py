class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        if rowIndex==0:
            return row

        for i in range(rowIndex):
            prevrow=[0]+row+[0]
            cur_row=[]
            for j in range(len(row)+1):
                cur_row.append(prevrow[j]+prevrow[j+1])
            row=cur_row
        return row

        