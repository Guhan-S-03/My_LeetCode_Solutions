class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ##here alsowe can do the simulation using queue
        #but we can use another logic that is
        #here actually the person at the kth indx not only needs his ticket no of time
        #to buy the tickets but it also depends on the other person timings
        #for example person at k-1 index is less than val at k then obviously he will 
        #buy before k and k waits for that k-1 val (time) if it is greater than val at k
        #then at the when k buys all k-1 also bought same tickets so we add the k val 
        #when we consider the index after the k in the queue k+1 if val at k+1 less than k
        #then he will buy before k and that val adds to result suppose if that val
        #greater or equal to k val then at the time when k boughts all he only boughts val-1 
        #in the index of k {that when k boughts all tickets what about others tickets}if we imagine 
        #that we can easily get the results

        res=0
        for i in range(len(tickets)):
            if i<=k:
                res+=min(tickets[i],tickets[k])
            else:
                res+=min(tickets[i],tickets[k]-1)
        return res

        