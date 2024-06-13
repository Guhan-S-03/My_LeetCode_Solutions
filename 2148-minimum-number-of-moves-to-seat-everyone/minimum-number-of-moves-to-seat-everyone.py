class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #we can sort the arrays so that we can get the closest seats plus 
        #minimize the no of moves
        #even mul students or seats in the same pos it works
        #we can also do counting sort becoz here no of pos is limited 
        #so we get lesser time complexity


        seats.sort()
        students.sort()
        res=0
        for i in range(len(seats)):
            res+=abs(students[i]-seats[i])
        return res

            

        

        