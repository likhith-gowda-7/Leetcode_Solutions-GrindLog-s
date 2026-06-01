class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=0
        for ch in set(s): #->O(26)=O(1)
            start=s.find(ch) #-> O(N)
            end=s.rfind(ch)  #->O(N)
            middle_elements=set(s[start+1:end])
            res+=len(middle_elements)
        return res
        