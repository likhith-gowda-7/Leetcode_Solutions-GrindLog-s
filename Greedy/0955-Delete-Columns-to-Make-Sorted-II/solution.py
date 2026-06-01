class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows=len(strs)
        cols=len(strs[0])
        state=[False]*rows
        deleted=0
        for col in range(cols):
            fine=True
            for row in range(1,rows):
                if(not state[row] and strs[row-1][col]>strs[row][col]):
                    deleted+=1
                    fine=False
                    break
            if(fine):
                for row in range(1,rows):
                    state[row]=state[row] or (strs[row-1][col]<strs[row][col])
        return deleted
                