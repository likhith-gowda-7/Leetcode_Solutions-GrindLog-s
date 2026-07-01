# 2812. Find the Safest Path in a Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid/)


## 📝 Problem Description

You are given a **0-indexed** 2D matrix `grid` of size `n x n`, where `(r, c)` represents:

	- A cell containing a thief if `grid[r][c] = 1`

	- An empty cell if `grid[r][c] = 0`

You are initially positioned at cell `(0, 0)`. In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The **safeness factor** of a path on the grid is defined as the **minimum** manhattan distance from any cell in the path to any thief in the grid.

Return *the **maximum safeness factor** of all paths leading to cell *`(n - 1, n - 1)`*.*

An **adjacent** cell of cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c - 1)`, `(r + 1, c)` and `(r - 1, c)` if it exists.

The **Manhattan distance** between two cells `(a, b)` and `(x, y)` is equal to `|a - x| + |b - y|`, where `|val|` denotes the absolute value of val.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2023/07/02/example1.png)
```

**Input:** grid = [[1,0,0],[0,0,0],[0,0,1]]
**Output:** 0
**Explanation:** All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

```

Example 2:**

![](https://assets.leetcode.com/uploads/2023/07/02/example2.png)
```

**Input:** grid = [[0,0,1],[0,0,0],[0,0,0]]
**Output:** 2
**Explanation:** The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2023/07/02/example3.png)
```

**Input:** grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
**Output:** 2
**Explanation:** The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

```

 

**Constraints:**

	- `1 <= grid.length == n <= 400`

	- `grid[i].length == n`

	- `grid[i][j]` is either `0` or `1`.

	- There is at least one thief in the `grid`.

## 🧠 Solution Explanation

**Intuition**
This solution uses a combination of Breadth-First Search (BFS) and a priority queue to find the maximum safeness factor of all paths leading to the bottom-right cell in the grid. The key insight is to first mark all thief cells and their adjacent cells with a value representing the minimum manhattan distance to the nearest thief. Then, use a priority queue to explore the grid in a way that maximizes the safeness factor.

**Approach**
1. If the top-left or bottom-right cell is a thief, return 0 as there is no path to the destination.
2. Initialize a set to keep track of visited cells and a deque to store thief cells.
3. Mark all thief cells and their adjacent cells with a value representing the minimum manhattan distance to the nearest thief.
4. Use a priority queue to explore the grid, starting from the top-left cell.
5. At each step, pop the cell with the minimum value from the priority queue and update the safeness factor.
6. If the current cell is the bottom-right cell, return the safeness factor.
7. Otherwise, add all unvisited adjacent cells to the priority queue and mark them as visited.

**Time Complexity**
O(n^2 * log n), where n is the size of the grid. The BFS step takes O(n^2) time, and the priority queue operations take O(log n) time per cell.

**Space Complexity**
O(n^2), where n is the size of the grid. The set and deque used to keep track of visited cells and thief cells take O(n^2) space.

**Key Insight**
The key insight is to use a priority queue to explore the grid in a way that maximizes the safeness factor. By always popping the cell with the minimum value from the priority queue, we ensure that we are always moving towards the cell with the maximum safeness factor. This approach allows us to efficiently explore the grid and find the maximum safeness factor.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2719 ms (Beats 83.24%) |
| 💾 Memory | 56.8 MB (Beats 23.99%) |
| 📅 Solved | 2026-07-01 |
| 💻 Language | Python |