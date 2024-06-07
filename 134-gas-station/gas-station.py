class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #there is greedy way to solve this
        #we will check whether we have enough gas to travel by sum gas>cost
        #if yes then we find the start index
        if sum(gas)<sum(cost):
            return -1

        total=0
        start=0

        for i in range(len(gas)):
            total +=(gas[i]-cost[i])
            if(total<0):
                total=0
                start=i+1
        return start
        