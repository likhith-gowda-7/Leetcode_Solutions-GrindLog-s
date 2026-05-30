class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n=len(s)
        if(s[-1]!="0"):
            return False
        reachable_count=[0]*n
        reachable_count[0]=1
        count=0
        for i in range(1,n):
            left=i-minJump
            right=i-maxJump
            if(left>=0):
                count+=reachable_count[left]
            if(right-1>=0):
                count-=reachable_count[right-1]
            if(count>0 and s[i]=="0"):
                reachable_count[i]=1
        return reachable_count[-1]==1
            