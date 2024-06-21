class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        intial_satisf=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                intial_satisf+=customers[i]
        
        max_cust,secret_window=0,intial_satisf

        for i in range(minutes):
            if grumpy[i]==1:
                secret_window+=customers[i]
        max_cust=secret_window
        
        for j in range(1,(len(grumpy)-minutes)+1):
            if grumpy[j-1]==1:
                secret_window-=customers[j-1]
            if grumpy[j+minutes-1]==1:
                secret_window+=customers[j+minutes-1]
                max_cust=max(max_cust,secret_window)
        return max_cust


        