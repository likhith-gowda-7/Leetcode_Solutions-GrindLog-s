class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for word in words:
            c=0
            for w in word:
                idx=ord(w)-97
                c+=weights[idx]
            ans+=chr((122-c%26))
        return ans