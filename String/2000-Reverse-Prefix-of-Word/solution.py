class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if(ch not in word):
            return word
        stack=[]
        res=""
        i=0
        while i<len(word):
            if(word[i]==ch):
                j="".join(stack[::-1])
                res=ch+j
                break
            else:
                stack.append(word[i])
            i+=1
        return res+"".join(word[i+1:])
        