class TrieNode:
    def __init__(self):
        self.ch = {}
        self.isEnd = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def add(self,s):
        curr = self.root
        for ch in s:
            if ch not in curr.ch:
                curr.ch[ch] = TrieNode()
            curr = curr.ch[ch]
        curr.isEnd = True

    def search(self,root,word):
        val=""
        for s in word:
            if s not in root.ch:
                return word
            val+=s
            root = root.ch[s]
            if(root.isEnd):
                break
        return val if(root.isEnd) else word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.add(word)
        sen = sentence.split(" ")
        res = []
        for word in sen:
            res.append(self.search(self.root,word))
        return " ".join(res)
