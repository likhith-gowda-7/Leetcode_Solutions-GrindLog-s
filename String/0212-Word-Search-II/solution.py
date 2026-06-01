class TrieNode:
    def __init__(self):
        self.map={}
        self.end=False
        self.word=None
class Solution:
    def __init__(self):
        self.root=TrieNode()

    def build(self,word):
        curr=self.root
        for w in word:
            if(w not in curr.map):
                curr.map[w]=TrieNode()
            curr=curr.map[w]
        curr.end=True
        curr.word=word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m=len(board)
        n=len(board[0])
        #building the Trie
        for word in words:
            self.build(word)
        res=[]
        def check(r,c):
            if(r<0 or r>=m or c<0 or c>=n):
                return True
            return False
        def backtrack(r,c,curr):
            if(check(r,c)):
                return 
            val=board[r][c]
            if(val not in curr.map):
                return
            curr=curr.map[val]
            if(curr.end):
                res.append(curr.word)
                curr.end=False
            board[r][c]="#"
            backtrack(r-1,c,curr)
            backtrack(r+1,c,curr)
            backtrack(r,c-1,curr)
            backtrack(r,c+1,curr)
            board[r][c]=val
        for r in range(m):
            for c in range(n):
                val=board[r][c]
                backtrack(r,c,self.root)
        return res


        
            
            