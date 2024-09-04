class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##there is a clever way that here we can do as many transactions
        #so whenever the price go from low to high we make a profit 
        #and here we can sell and buy on same day so we count every stairstep

        profit=0

        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=(prices[i]-prices[i-1])
        return profit

        