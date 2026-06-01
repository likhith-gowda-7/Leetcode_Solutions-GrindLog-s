class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k=1
        "Formula"
        x=num1-(k*num2)
        while x>=0:
            if(bin(x).count("1")<=k<=x):
                return k
            k+=1
            x=num1-(k*num2)
        return -1
