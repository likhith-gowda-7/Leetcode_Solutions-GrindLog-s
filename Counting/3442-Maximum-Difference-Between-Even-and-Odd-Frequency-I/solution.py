class Solution:
    def maxDifference(self, s: str) -> int:
        h1=Counter(s)
        even=float("inf")
        odd=0
        for key,val in h1.items():
            if(val%2):
                odd=max(odd,val)
            else:
                even=min(even,val)
        return odd-even
            
