class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time=0
        n=len(colors)
        curr=neededTime[0]
        maxi=neededTime[0]
        for i in range(1,n):
            if(colors[i]==colors[i-1]):
                curr+=neededTime[i]
                maxi=max(maxi,neededTime[i])
            else:
                time=curr-maxi
                min_time+=time
                curr=neededTime[i]
                maxi=neededTime[i]
        min_time+=curr-maxi
        return min_time