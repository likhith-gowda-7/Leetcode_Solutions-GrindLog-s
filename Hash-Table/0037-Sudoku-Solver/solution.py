class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows=defaultdict(set)
        cols=defaultdict(set)
        sub_boxes=defaultdict(set)
        empty_spots=[]
        #given sudoku will always be valid so no need to check for valid!!!
        for r in range(9):
            for c in range(9):
                #this for sub_boxes(3x3)
                key=(r//3,c//3)
                val=board[r][c]
                if(val!="."):
                    rows[r].add(val)
                    cols[c].add(val)
                    sub_boxes[key].add(val)
                #this tells that this spot need to filled
                else:
                    empty_spots.append((r,c))
        #this part is just for optimization and pruning
        def choices_left(r,c):
            invalid=len(set.union(rows[r],cols[c],sub_boxes[r//3,c//3]))
            #this gives us available choice of numbers
            return 9-invalid
        #then we sort empty spots array based spot that has minimum number choices
        empty_spots.sort(key=lambda pos:choices_left(pos[0],pos[1]))
        n=len(empty_spots)
        #this backtrack goes to every empty spots and try to add the valid number to it
        def backtrack(idx):
            if(idx==n):
                return True
            #we'll try to add every number in range of(1-9) and pick the right one
            r,c=empty_spots[idx]
            for num in range(1,10):
                key=(r//3,c//3)
                val=str(num)
                #this checks for validation
                if((val in rows[r] or val in cols[c]) or (val in sub_boxes[key])):
                    continue
                else:
                    board[r][c]=val
                    rows[r].add(val)
                    cols[c].add(val)
                    sub_boxes[key].add(val)
                    if(backtrack(idx+1)):
                        return True
                    #undo
                    board[r][c]="."
                    rows[r].remove(val)
                    cols[c].remove(val)
                    sub_boxes[key].remove(val)
            return False
        backtrack(0)
