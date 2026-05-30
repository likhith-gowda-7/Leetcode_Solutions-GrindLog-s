class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res=0
        prev=0
        for i in range(len(s)):
            curr=roman[s[i]]
            if(prev<curr):
                res-=prev
                res+=curr-prev
            else:
                res+=curr
            prev=roman[s[i]]
        return res