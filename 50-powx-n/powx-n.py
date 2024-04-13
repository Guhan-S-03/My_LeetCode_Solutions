class Solution:
    def myPow(self, x: float, n: int) -> float:
        #its a simple mul but here the edge case is we have neg pow
        #so in that case we take 1/ans , recurvise fun for mul to avoid 
        #repetetive mul of num
        def poww(x,n):
            if x==0:
                return 0
            if n==0:
                return 1

            res=poww(x,n//2)
            res=res*res
            return res *x if n%2 else res
        val=poww(x,abs(n))
        return val if n>=0 else 1/val

        