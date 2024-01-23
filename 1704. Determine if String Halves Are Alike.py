class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        split=n//2
        avow=0
        bvow=0
        for i in range(split):
            if(s[i] in {'a','e','i','o','u','A','E','I','O','U'}):
                avow+=1
            if(s[i+split] in {'a','e','i','o','u','A','E','I','O','U'}):
                bvow+=1
        if(avow==bvow):
            return True
        else:
            return False

        