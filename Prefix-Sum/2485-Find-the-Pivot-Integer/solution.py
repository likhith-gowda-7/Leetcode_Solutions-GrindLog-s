class Solution:
    def pivotInteger(self, n: int) -> int:
        total=sum(range(n+1))
        left=0
        for i in range(1,n+1):
            right=total-left
            left+=i
            if(right==left):
                return i
        return -1
