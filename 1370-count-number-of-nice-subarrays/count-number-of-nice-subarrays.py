class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ##actually it is two pointer sliding window concepts
        #but the thing is we need to find how many diff subarray
        #that can be formed within this l->r ,so we need another pointer
        #m that travels upto the first odd value and take the diff to find those val
        #and shift the left only if req odd val exceeds k
        #m always with l

        l,m,r=0,0,0
        odd,res=0,0

        for r in range(len(nums)):
            if nums[r]%2:
                odd+=1
            
            while odd>k:
                if nums[l]%2:
                    odd-=1
                l+=1
                m=l
            if odd==k:
                while not nums[m]%2:
                    m+=1
                res+=(m-l)+1
        return res

        