class Solution(object):
    def lengthOfLongestSubstring(self, s):
        check=set()
        l=0
        maxi=0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1
            check.add(s[r])
            maxi=max(maxi,r-l+1)
        return maxi

            