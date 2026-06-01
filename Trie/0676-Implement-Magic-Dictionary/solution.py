class TrieNode:
    def __init__(self):
        self.map={}
        self.isEnd=False

class MagicDictionary:

    def __init__(self):
        self.root=TrieNode()
    def add(self,word):
        n=len(word)
        curr=self.root
        if(n not in curr.map):
            curr.map[n]=TrieNode()
        curr=curr.map[n]
        for c in word:
            if(c not in curr.map):
                curr.map[c]=TrieNode()
            curr=curr.map[c]
        curr.isEnd=True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.add(word)
        
    def search(self, searchWord: str) -> bool:
        n=len(searchWord)
        curr=self.root
        if(n not in curr.map):
            return False
        curr=curr.map[n]
        def dfs(root,i,c):
            if(i==n):
                return root.isEnd and c
            w=searchWord[i]
            for key,val in root.map.items():
                if(key==w):
                    if(dfs(val,i+1,c)):
                        return True
                else:
                    if(not c and dfs(val,i+1,True)):
                        return True
            return False
        return dfs(curr,0,False)
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)