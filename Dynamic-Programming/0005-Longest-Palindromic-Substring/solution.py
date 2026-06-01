class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand(l,r):
            #here we expand from the center for searching the palindrome
            while (l>=0 and r<n) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        res=""
        for i in range(n):
            #Here the palindrome can be formed of two types:
            '''1.odd length -> considering the current character as a center of the palindrome string
            and then expanding outwards'''
            odd_length_palindrome=expand(i,i)
            '''2.Even length -> assuming the palindrome will be of even length
            so we compare with current character with next character
            and then expanding outwards'''
            even_length_palindrome=expand(i,i+1)
            if(len(odd_length_palindrome)>len(res)):
                res=odd_length_palindrome
            if(len(even_length_palindrome)>len(res)):
                res=even_length_palindrome
        return res