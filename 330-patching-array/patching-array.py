class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        #we want to patch some elements so that finally we 
        #can able to get the values in the range[1:n]==[0:n]
        #intially [0,0] every time we update our end range while we traverse
        #through the gven list in asc order..that indicates [0,n] we can actually create
        #if we encounter ele in array that is >end+1 means we cant make end+1 in our range 
        #so obviously we patch that and finally we need that min no of patches

        i,patches,end=0,0,0

        while end<n:
            if i<len(nums) and nums[i]<=end+1:
                end+=nums[i]
                i+=1
            else:
                patches+=1
                end+=(end+1)
        return patches


        