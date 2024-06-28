class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ## we are going to assign values to the node based on the freq of road that it appears
        city_freq=[0]*n

        for c1,c2 in roads:
            city_freq[c1]+=1
            city_freq[c2]+=1
        
        res=0
        val_assign=1 #this is the val that we r assigning to the min freq city(start)
        ## we can use some technique here that is if we assign 0th city of val 4 means
        #then in the tot this val 4 is added for the freq of 0th city 

        for freq in sorted(city_freq):
            res+=(freq*val_assign)
            val_assign+=1
        return res
        