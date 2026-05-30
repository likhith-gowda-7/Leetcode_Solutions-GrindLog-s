class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1_sum=0
        num2_sum=0
        for i in range(1,n+1):
            if(i%m!=0):
                num1_sum+=i
            else:
                num2_sum+=i
        return num1_sum-num2_sum