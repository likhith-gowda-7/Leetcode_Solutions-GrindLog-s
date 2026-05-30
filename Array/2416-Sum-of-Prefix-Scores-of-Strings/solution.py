class TrieNode:
    def __init__(self):
        self.map={}
        self.count=0

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def build(self,word):
        curr=self.root
        for ch in word:
            if ch not in curr.map:
                curr.map[ch]=TrieNode()
            curr=curr.map[ch]
            curr.count+=1

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        length=len(words)
        for i in range(length):
            self.build(words[i])
        curr=self.root

        def get_score(root,i,c):
            if(i==l):
                return c
            root=root.map[word[i]]
            val=root.count
            return get_score(root,i+1,c+val)
        res=[]
        for i in range(length):
            c=0
            l=len(words[i])
            word=words[i]
            c=get_score(curr,0,0)
            res.append(c)
        return res

            