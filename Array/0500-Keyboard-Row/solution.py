class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keys=set()
        keys.add("qwertyuiop")
        keys.add("asdfghjkl")
        keys.add("zxcvbnm")
        res=[]
        for word in words:
            val=word.lower()
            for k in keys:
                ch=True
                for i in val:
                    if(i in k):
                        ch=True
                    else:
                        ch=False
                        break
                if(ch):
                    res.append(word)
                    break
        return res

        
        
        