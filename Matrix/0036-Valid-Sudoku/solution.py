class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        sub_boxes=defaultdict(set)
        for row in range(9):
            for col in range(9):
                if(board[row][col]!="."):
                    val=board[row][col]
                    sub_row=row//3
                    sub_col=col//3
                    if(val in sub_boxes[(sub_row,sub_col)]):
                        return False
                    if(val in rows[row]):
                        return False
                    if(val in cols[col]):
                        return False
                    sub_boxes[(sub_row,sub_col)].add(val)
                    rows[row].add(val)
                    cols[col].add(val)
        return True