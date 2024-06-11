class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #we need a res in which the element appears in the order in
        #which it is appeared at a2
        #hashmap for storing the freq helps to build the res array

        arr2set=set(arr2) ##searching in set is efficient than in a array
        count_a1=defaultdict(int)
        end=[]

        for n in arr1:
            if n not in arr2set:
                end.append(n)
            count_a1[n]+=1
        end.sort()

        res=[]
        for n in arr2:
            for i in range(count_a1[n]):
                res.append(n)
        return res+end

            



        