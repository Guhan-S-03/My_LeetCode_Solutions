class Solution:
    def reverse(self, x: int) -> int:
        minn=-2147483648
        maxx=2147483647
        res=0

        while x:
            lval=int(math.fmod(x,10))
            x=int(x/10)

            if (res>maxx//10 or (res==maxx//10 and lval>=maxx%10)):
                return 0
            if (res<minn//10 or (res==minn//10 and lval<=minn%10)):
                return 0
            res=(res*10)+lval
        return res
