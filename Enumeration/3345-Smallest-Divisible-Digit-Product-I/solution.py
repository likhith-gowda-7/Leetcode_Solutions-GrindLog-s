class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            curr=1
            num=i
            while num:
                last=num%10
                curr*=last
                num//=10
            if(curr%t==0):
                return i
        
        