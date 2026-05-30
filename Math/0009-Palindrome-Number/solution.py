class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        def rev(num):
            reversed_num=0
            while num:
                last=num%10
                num//=10
                reversed_num=(reversed_num*10)+last
            return reversed_num
        return x==rev(x)

        