class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res=0
        for val in patterns:
            if(val in word):
                res+=1
        return res