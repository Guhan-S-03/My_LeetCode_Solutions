class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        #here also we r doing sliding window
        #and we are making the array to 1 from left so whenever we find 0 we 
        #need to change them to 1 so for that we need subarry of size k 
        #then only we can change otherwise -1
        #also we keep track of fliping index in the queue thats tells us the
        #current index actual flipped value with the help of mod opr
        #and if the q contains any index which is out of range from current index
        #then we need to pop them

        q=deque()#going to store the flipped indexs
        res=0

        for i in range(len(nums)):
            while q and i>q[0]+k-1:#means that index at q will not flip our current indx
                q.popleft()

            if (nums[i]+len(q))%2==0:#this mod2 actually indicates only 2 possible values and this indicates the current updated val
                if i+k>len(nums):
                    return -1
                res+=1
                q.append(i)
        return res 




