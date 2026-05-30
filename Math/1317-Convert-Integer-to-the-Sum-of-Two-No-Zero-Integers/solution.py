class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def zero_check(num):
            while num:
                last=num%10
                if(last==0):
                    return True
                num//=10
            return False
        for num1 in range(1,n):
            num2=n-num1
            if(not zero_check(num1) and not zero_check(num2)):
                return [num1,num2]            