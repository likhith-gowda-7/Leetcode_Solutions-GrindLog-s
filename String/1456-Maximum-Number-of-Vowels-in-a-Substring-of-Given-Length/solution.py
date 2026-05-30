class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        max_sum=0
        curr=0
        v={'a','e','i','o','u'}
        for r in range(len(s)):
            if(s[r] in v):
                curr+=1
            if(r-l+1>k):
                if(s[l] in v):
                    curr-=1
                l+=1
            if(curr>max_sum):
                max_sum=curr
        return max_sum
                
        
        