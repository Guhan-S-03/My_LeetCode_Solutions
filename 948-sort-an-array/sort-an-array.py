class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort ...calling merge sort on left and right then merge the both to get complete sorted list
        def merge(arr,l,m,r):
            left,right=arr[l:m+1],arr[m+1:r+1]
            i,j,k=l,0,0

            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                arr[i]=left[j]
                j+=1
                i+=1
            while k<len(right):
                arr[i]=right[k]
                k+=1
                i+=1
            return arr


        def mergesort(arr,l,r):
            if l==r:
                return arr
            
            m=(l+r)//2
            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            merge(arr,l,m,r)
            return arr

        return mergesort(nums,0,len(nums)-1)