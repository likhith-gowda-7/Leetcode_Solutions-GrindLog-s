class TrieNode:
    def __init__(self):
        self.ch={}
        self.End_of_word=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if(c not in curr.ch):
                curr.ch[c]=TrieNode()
            curr=curr.ch[c]
        curr.End_of_word=True
    def search(self, word: str) -> bool:
        curr=self.root
        l=len(word)
        def dfs(root,i):
            if(i==l):
                return root.End_of_word
            if(word[i]=="."):
                for val in root.ch.values():
                    if(dfs(val,i+1)):
                        return True
                return False
            else:
                if(word[i] not in root.ch):
                    return False
                root=root.ch[word[i]]
            return dfs(root,i+1)   
        return dfs(curr,0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)