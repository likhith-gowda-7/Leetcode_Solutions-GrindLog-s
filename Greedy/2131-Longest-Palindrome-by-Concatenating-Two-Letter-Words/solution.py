class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        h1=Counter(words)
        res=0
        is_exits=False
        for key in h1.keys():
            rev=key[1]+key[0]
            if(key==rev):
                pairs=h1[key]//2
                res+=pairs*4
                if(not is_exits and h1[key]%2):
                    is_exits=True
            else:
                res+=min(h1[key],h1[rev])*2

        if(is_exits):
            res+=2
        return res
                
        