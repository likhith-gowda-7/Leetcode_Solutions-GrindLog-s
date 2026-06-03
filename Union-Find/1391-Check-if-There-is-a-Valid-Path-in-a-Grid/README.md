> 📌 **Cross-listed:** Primary location is [Array/1391-Check-if-There-is-a-Valid-Path-in-a-Grid](../../Array/1391-Check-if-There-is-a-Valid-Path-in-a-Grid). This problem also appears under: **Array**, **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Matrix**

# 1391. Check if There is a Valid Path in a Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/)


## 📝 Problem Description

You are given an `m x n` `grid`. Each cell of `grid` represents a street. The street of `grid[i][j]` can be:

	- `1` which means a street connecting the left cell and the right cell.

	- `2` which means a street connecting the upper cell and the lower cell.

	- `3` which means a street connecting the left cell and the lower cell.

	- `4` which means a street connecting the right cell and the lower cell.

	- `5` which means a street connecting the left cell and the upper cell.

	- `6` which means a street connecting the right cell and the upper cell.

![](https://assets.leetcode.com/uploads/2020/03/05/main.png)
You will initially start at the street of the upper-left cell `(0, 0)`. A valid path in the grid is a path that starts from the upper left cell `(0, 0)` and ends at the bottom-right cell `(m - 1, n - 1)`. **The path should only follow the streets**.

**Notice** that you are **not allowed** to change any street.

Return `true`* if there is a valid path in the grid or *`false`* otherwise*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/03/05/e1.png)
```

**Input:** grid = [[2,4,3],[6,5,2]]
**Output:** true
**Explanation:** As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/03/05/e2.png)
```

**Input:** grid = [[1,2,1],[1,2,1]]
**Output:** false
**Explanation:** As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)

```

Example 3:**

```

**Input:** grid = [[1,1,2]]
**Output:** false
**Explanation:** You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 300`

	- `1 <= grid[i][j] <= 6`

## 🧠 Solution Explanation

**Intuition**
This solution uses a breadth-first search (BFS) approach to explore all possible paths from the starting cell to the bottom-right cell. The key insight is that we can use the given grid values to determine the valid directions to move in each cell, and then use a queue to keep track of the cells to visit next.

**Approach**
1. Define a dictionary `directions` to map each grid value to its corresponding valid directions.
2. Initialize a 2D boolean array `seen` to keep track of visited cells.
3. Create a queue `q` and add the starting cell `(0, 0)` to it.
4. While the queue is not empty, pop the next cell `(row, col)` from the queue.
5. If the popped cell is the bottom-right cell, return `True`.
6. For each valid direction `r, c` from the current cell, calculate the new cell coordinates `ro, co`.
7. If the new cell is within the grid boundaries and has not been visited, check if the direction `r, c` is valid for the new cell's grid value.
8. If the direction is valid, add the new cell to the queue and mark it as visited.
9. If the queue is empty after exploring all cells, return `False`.

**Time Complexity**
O(m \* n), where m and n are the dimensions of the grid. This is because we visit each cell at most once.

**Space Complexity**
O(m \* n), where m and n are the dimensions of the grid. This is because we use a 2D boolean array `seen` to keep track of visited cells, which requires O(m \* n) space.

**Key Insight**
The key to this solution is the ability to determine valid directions for each cell based on its grid value. By using the `directions` dictionary, we can efficiently explore all possible paths from the starting cell to the bottom-right cell.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 147 ms (Beats 70.13%) |
| 💾 Memory | 24.7 MB (Beats 71.57%) |
| 📅 Solved | 2026-04-27 |
| 💻 Language | Python |