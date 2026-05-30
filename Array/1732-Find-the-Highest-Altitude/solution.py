class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        maxi=0
        for val in gain:
            alt+=val
            maxi=max(alt,maxi)
        return maxi
           