class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split()
        res=0
        for word in words:
            invalid=False
            for w in brokenLetters:
                if(w in word):
                    invalid=True
                    break
            if(not invalid):
                res+=1
        return res