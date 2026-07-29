class Solution:
    def smallestPalindrome(self, s: str) -> str:
        h1=Counter(s)
        res=""
        mid=""
        for i in range(26):
            ch=chr(97+i)
            if(h1[ch]>0):
                if(h1[ch]%2==1):
                    mid=ch
                res+=(ch)*(h1[ch]//2)
        return res+mid+res[::-1]

        
        
