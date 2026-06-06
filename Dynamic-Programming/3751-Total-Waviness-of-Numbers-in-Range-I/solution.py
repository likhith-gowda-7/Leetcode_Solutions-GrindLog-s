class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(num):
            right=num%10
            num//=10
            curr=num%10
            num//=10
            left=0
            wave=0
            while num:
                left=num%10
                if(left>curr<right or left<curr>right):
                    wave+=1
                num//=10
                right,curr=curr,left
            return wave
        res=0
        for number in range(max(101,num1),num2+1):
            res+=solve(number)
        return res