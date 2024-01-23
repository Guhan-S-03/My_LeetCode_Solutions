class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        highalt=0
        for i in gain:
            alt+=i
            highalt=max(highalt,alt)
        return highalt

        