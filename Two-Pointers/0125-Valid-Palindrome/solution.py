class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal=""
        for i in s.lower():
            if(i.isalnum()):
                pal+=i
        return pal==pal[::-1]


