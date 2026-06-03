# 37. Sudoku Solver


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sudoku-solver/)


## 📝 Problem Description

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

	- Each of the digits `1-9` must occur exactly once in each row.

	- Each of the digits `1-9` must occur exactly once in each column.

	- Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

 

Example 1:**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
```

**Input:** board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
**Output:** [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
**Explanation:** The input board is shown above and the only valid solution is shown below:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

```

 

**Constraints:**

	- `board.length == 9`

	- `board[i].length == 9`

	- `board[i][j]` is a digit or `'.'`.

	- It is **guaranteed** that the input board has only one solution.

## 🧠 Solution Explanation

### Intuition
The Sudoku solver works by utilizing a backtracking approach to fill in the empty cells of the Sudoku puzzle. It starts by initializing sets to keep track of the numbers present in each row, column, and 3x3 sub-box. The algorithm then sorts the empty spots based on the number of choices available for each spot, which helps in pruning the search space.

### Approach
1. Initialize sets for rows, columns, and sub-boxes to keep track of the numbers present in each.
2. Identify and store the empty spots in the Sudoku puzzle.
3. Sort the empty spots based on the number of choices available for each spot.
4. Implement a backtracking function that tries to fill in each empty spot with a valid number (1-9).
5. For each empty spot, check if a number is valid by ensuring it does not already exist in the same row, column, or sub-box.
6. If a valid number is found, recursively call the backtracking function for the next empty spot.
7. If no valid number is found, undo the changes made and return False to trigger backtracking.

### Time Complexity
The time complexity is O(9^(n*n)), where n is the size of the Sudoku puzzle (n=3 for a standard 9x9 puzzle). This is because in the worst-case scenario, the algorithm has to try all possible numbers for each empty spot.

### Space Complexity
The space complexity is O(n*n), where n is the size of the Sudoku puzzle. This is due to the storage required for the sets of rows, columns, and sub-boxes, as well as the recursive call stack.

### Key Insight
The key insight behind this solution is the use of backtracking to efficiently explore the vast search space of possible Sudoku solutions. By sorting the empty spots based on the number of choices available, the algorithm can prune the search space and reduce the number of recursive calls, making the solution more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1509 ms (Beats 58.73%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-08-31 |
| 💻 Language | Python |