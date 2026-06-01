class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_length=len(word)
        m=len(board)
        n=len(board[0])
        def backtrack(i,j,word_idx):
            #this tells we have found the word
            if(word_idx==word_length):
                return True
            if((i<0 or i>=m) or (j<0 or j>=n)):
                return False
            if(word[word_idx]!=board[i][j]):
                return False
            #changing the orginal value so that it should not be keeped again
            board[i][j]="#"
            #Up,Down,Left,Right
            found=(backtrack(i-1,j,word_idx+1) or backtrack(i+1,j,word_idx+1) or backtrack(i,j-1,word_idx+1) or backtrack(i,j+1,word_idx+1)) 
            #undo the changes
            board[i][j]=word[word_idx]
            return found
        for i in range(m):
            for j in range(n):
                if(board[i][j]==word[0] and backtrack(i,j,0)):
                    return True
        return False
            
            