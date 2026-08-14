class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq=defaultdict(int)
        l=0
        sub_len=0
        res=2
        for r in range(len(s)):
            freq[s[r]]+=1
            sub_len+=1
            while freq[s[r]]>2:
                freq[s[l]]-=1
                sub_len-=1
                l+=1
            if(sub_len>res):
                res=sub_len
        return res
