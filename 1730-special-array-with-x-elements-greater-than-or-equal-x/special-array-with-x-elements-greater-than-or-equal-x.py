class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ##so x ele greater than or equal to x
        #obviously the sol in the range(1-len(nums)) becoz the max possible value 
        #so make a array with the index uptothat len
        #then count the no no of ele which is >= to that index

        count=[0]*(len(nums)+1)
        ##here actually at every index we add from the indx next to them to chk tot no of val
        #>= to that indx
        for n in nums:
            index= n if n<len(nums) else len(nums)
            count[index]+=1
        tot_right_ele=0

        for i in range(len(nums),-1,-1):
            tot_right_ele+=count[i]
            if i==tot_right_ele:
                return i
        return -1
        