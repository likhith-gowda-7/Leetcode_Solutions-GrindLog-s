class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        #At every step check if the number is divisble by 3
        while n>1:
            if(n%3==0):
                n//=3
            else:
                return False
        return True