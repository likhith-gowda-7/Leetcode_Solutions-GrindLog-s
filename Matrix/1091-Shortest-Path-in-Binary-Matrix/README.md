> 📌 **Cross-listed:** Primary location is [Array/1091-Shortest-Path-in-Binary-Matrix](../../Array/1091-Shortest-Path-in-Binary-Matrix). This problem also appears under: **Array**, **Breadth-First Search**, **Matrix**

# 1091. Shortest Path in Binary Matrix


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix/)


## 📝 Problem Description

Given an `n x n` binary matrix `grid`, return *the length of the shortest **clear path** in the matrix*. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

	- All the visited cells of the path are `0`.

	- All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)
```

**Input:** grid = [[0,1],[1,0]]
**Output:** 2

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)
```

**Input:** grid = [[0,0,0],[1,1,0],[1,1,0]]
**Output:** 4

```

Example 3:**

```

**Input:** grid = [[1,0,0],[1,1,0],[1,1,0]]
**Output:** -1

```

 

**Constraints:**

	- `n == grid.length`

	- `n == grid[i].length`

	- `1 <= n <= 100`

	- `grid[i][j] is 0 or 1`

## 🧠 Solution Explanation

**Intuition**
The solution uses a breadth-first search (BFS) approach to find the shortest clear path in the binary matrix. It starts from the destination cell (bottom-right) and tries to reach the source cell (top-left) by exploring all possible 8-directional paths. The key insight is to invert the thinking process and start from the destination, which simplifies the problem and makes it easier to find the shortest path.

**Approach**
1. Check if the source or destination cell is blocked (1), in which case return -1.
2. Define a helper function `check` to verify if a cell is within the grid boundaries and not blocked.
3. Initialize a queue `q` with the destination cell and its distance (1).
4. Mark the destination cell as visited by setting its value to 1.
5. Define all 8 possible directions for the BFS exploration.
6. While the queue is not empty, dequeue a cell and check if it's the target cell. If it is, return its distance.
7. For each neighboring cell in the 8 directions, check if it's valid using the `check` function. If it is, mark it as visited and enqueue it with its distance incremented by 1.

**Time Complexity**
O(n^2) where n is the size of the grid. This is because in the worst case, we need to visit all cells in the grid to find the shortest path.

**Space Complexity**
O(n^2) where n is the size of the grid. This is because in the worst case, we need to store all cells in the queue.

**Key Insight**
The key insight is to invert the thinking process and start from the destination cell, which simplifies the problem and makes it easier to find the shortest path. This approach avoids the need to keep track of the source cell and its distance, making the algorithm more efficient and easier to implement.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 163 ms (Beats 57.69%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-08-31 |
| 💻 Language | Python |