class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        #we need to find out the maximum possible min dist between two balls
        #min dist in the sense lets take mind=3 if one ball is in pos 2 then next ball
        #should be at pos 5 min dist 2---5 is 3 :: guaranteed that there exist 2 balls
        #in that way we need to find the max val of min dist in that we can place all the balls
        position.sort()

        def can_we_place_all_balls(mindist):
            nofballs=1
            prevpos=position[0]
            for i in range(1,len(position)):
                if position[i]-prevpos>=mindist:
                    nofballs+=1
                    prevpos=position[i]
            return nofballs>=m

        def binarysearchdist():
            #here the dist bet balls must be in the range 1-position[-1]
            l,r=0,position[-1]
            ans=-1

            while l<=r:
                mid=(l+r)//2 ##mid is the min dist that we are going to check
                if can_we_place_all_balls(mid):
                    l=mid+1
                    ans=mid
                else:
                    r=mid-1
            return ans
        return binarysearchdist()

