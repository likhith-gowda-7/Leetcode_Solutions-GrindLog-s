class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        h1={}
        def char_count(w):
            ch=[0]*26
            for c in w:
                i=ord(c)-97
                ch[i]+=1
            h1[w]=ch
        stack=[]
        for word in words:
            char_count(word)
            stack.append(word)
            while len(stack)>1 and h1[stack[-1]]==h1[stack[-2]]:
                stack.pop()
        return stack