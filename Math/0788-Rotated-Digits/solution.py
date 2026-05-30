class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid={2,5,6,9}
        def rev(num):
            change=0
            while num:
                last=num%10
                if(last==3 or last==4 or last==7):
                    return 0
                elif(last in valid):
                    change=1
                num//=10
            return change
        total=0
        for number in range(1,n+1):
            total+=rev(number)
        return total