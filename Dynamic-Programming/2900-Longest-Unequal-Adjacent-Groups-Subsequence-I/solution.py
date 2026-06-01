class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        search=0 if(groups[0]==1) else 1
        res=[words[0]]
        for i in range(1,len(words)):
            if(groups[i]==search):
                res.append(words[i])
                search=0 if(groups[i]==1) else 1
        return res