class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for s in zip(*strs):
            if(sorted(s)!=list(s)):
                count+=1
        return count
