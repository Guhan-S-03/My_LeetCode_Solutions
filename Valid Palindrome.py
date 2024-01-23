class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowers=s.lower()
        alpnums="".join(char for char in lowers if char.isalnum())
        revstr=alpnums[::-1]
        if(alpnums==revstr):
            return True
        else:
            return False

        