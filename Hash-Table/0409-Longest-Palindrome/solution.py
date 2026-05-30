class Solution:
    def longestPalindrome(self, s: str) -> int:
        pair=set()
        max_len=0
        for i in s:
            if(i in pair):
                max_len+=2
                pair.remove(i)
            else:
                pair.add(i)
        if(pair):
            max_len+=1
        return max_len