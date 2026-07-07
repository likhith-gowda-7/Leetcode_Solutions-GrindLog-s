class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digit_sum=0
        x=0
        n=int(str(n)[::-1])
        while n:
            last=n%10
            if(last!=0):
                digit_sum+=last
                x+=last
                x*=10
            n//=10
        x//=10
        return x*digit_sum
