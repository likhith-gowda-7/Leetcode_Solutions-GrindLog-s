class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        h1=defaultdict(int)
        maxi=0
        for i in range(len(s)):
            h1[s[i]]+=1
            diff=abs(h1["N"]-h1["S"])+abs(h1["E"]-h1["W"])
            #to avoid going further than current movement
            mini=min(diff+k*2,i+1)
            maxi=max(maxi,mini)
        return maxi