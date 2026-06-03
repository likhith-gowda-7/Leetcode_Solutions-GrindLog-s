> 📌 **Cross-listed:** Primary location is [Array/0130-Surrounded-Regions](../../Array/0130-Surrounded-Regions). This problem also appears under: **Array**, **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Matrix**

# 130. Surrounded Regions


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/surrounded-regions/)


## 📝 Problem Description

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

	- **Connect**: A cell is connected to adjacent cells horizontally or vertically.

	- **Region**: To form a region **connect every** `'O'` cell.

	- **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed **by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

 

Example 1:**

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:**

**Input:** board = [["X"]]

**Output:** [["X"]]

 

**Constraints:**

	- `m == board.length`

	- `n == board[i].length`

	- `1 <= m, n <= 200`

	- `board[i][j]` is `'X'` or `'O'`.

## 🧠 Solution Explanation

## Intuition
The solution works by first identifying all the 'O' regions connected to the border of the board, then marking them as visited. This is because any 'O' region that is not connected to the border must be surrounded by 'X' cells. By doing so, we can easily distinguish between surrounded and non-surrounded 'O' regions.

## Approach
1. Initialize a queue to store the border 'O' cells.
2. Iterate over the border cells, and for each 'O' cell found, mark it as visited and add it to the queue.
3. Perform a multi-source BFS from all the border 'O' cells, marking all connected 'O' cells as visited.
4. Finally, iterate over the board and flip the 'O' regions: if an 'O' cell is not marked as visited, it must be surrounded, so replace it with 'X'; otherwise, restore the marked 'O' cells to their original state.

## Time Complexity
The time complexity is O(m*n), where m and n are the dimensions of the board. This is because in the worst case, we need to visit every cell on the board once during the BFS and once during the final iteration.

## Space Complexity
The space complexity is also O(m*n), as in the worst case, the queue can store all the cells on the board (e.g., when the entire board is filled with 'O' cells).

## Key Insight
The key insight here is to use a temporary marker ('B') to distinguish between 'O' cells that are connected to the border and those that are not. This allows us to easily identify and capture the surrounded 'O' regions in a single pass over the board.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 21.7 MB (Beats 99.95%) |
| 📅 Solved | 2025-12-17 |
| 💻 Language | Python |