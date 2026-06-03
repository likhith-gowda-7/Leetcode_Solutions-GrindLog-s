# 36. Valid Sudoku


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/valid-sudoku/)


## 📝 Problem Description

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

	- Each row must contain the digits `1-9` without repetition.

	- Each column must contain the digits `1-9` without repetition.

	- Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

	- A Sudoku board (partially filled) could be valid but is not necessarily solvable.

	- Only the filled cells need to be validated according to the mentioned rules.

 

Example 1:**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
```

**Input:** board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
**Output:** true

```

Example 2:**

```

**Input:** board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
**Output:** false
**Explanation:** Same as Example 1, except with the **5** in the top left corner being modified to **8**. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

```

 

**Constraints:**

	- `board.length == 9`

	- `board[i].length == 9`

	- `board[i][j]` is a digit `1-9` or `'.'`.

## 🧠 Solution Explanation

## Intuition
The approach to solving this problem involves checking each row, column, and 3x3 sub-box for duplicate values. This works because a Sudoku board is valid if and only if each row, column, and sub-box contains the digits 1-9 without repetition. By using sets to store the values in each row, column, and sub-box, we can efficiently check for duplicates.

## Approach
1. Initialize sets for each row, column, and sub-box using a dictionary with default values as sets.
2. Iterate over each cell in the Sudoku board.
3. If a cell is not empty, check if its value already exists in the corresponding row, column, or sub-box.
4. If a duplicate value is found, immediately return False.
5. Otherwise, add the value to the corresponding row, column, and sub-box sets.
6. If the entire board is iterated over without finding any duplicate values, return True.

## Time Complexity
The time complexity is O(1), which may seem counterintuitive, but it's because the size of the input (a 9x9 Sudoku board) is constant. In terms of the number of cells, it's O(81), but since the size of the board is fixed, it's considered constant time.

## Space Complexity
The space complexity is O(1) as well, because the maximum amount of space used does not grow with the size of the input. The space used is proportional to the number of rows, columns, and sub-boxes, which is constant for a 9x9 Sudoku board.

## Key Insight
The key insight here is to use sets to store the values in each row, column, and sub-box, allowing for efficient duplicate checking. This approach takes advantage of the constant size of the Sudoku board, making it possible to solve the problem in constant time and space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2 ms (Beats 80.37%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-08-30 |
| 💻 Language | Python |