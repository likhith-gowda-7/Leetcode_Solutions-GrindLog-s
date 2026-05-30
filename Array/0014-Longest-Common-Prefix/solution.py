class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        l=len(prefix)
        for s in strs[1:]:
            while prefix!=s[:l]:
                l-=1
                if(l==0):
                    return ""
                prefix=prefix[:l]
        return prefix