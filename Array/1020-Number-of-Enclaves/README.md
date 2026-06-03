# 1020. Number of Enclaves


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-enclaves/)


## 📝 Problem Description

You are given an `m x n` binary matrix `grid`, where `0` represents a sea cell and `1` represents a land cell.

A **move** consists of walking from one land cell to another adjacent (**4-directionally**) land cell or walking off the boundary of the `grid`.

Return *the number of land cells in* `grid` *for which we cannot walk off the boundary of the grid in any number of **moves***.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg)
```

**Input:** grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
**Output:** 3
**Explanation:** There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg)
```

**Input:** grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
**Output:** 0
**Explanation:** All 1s are either on the boundary or can reach the boundary.

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 500`

	- `grid[i][j]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to count the number of land cells in a given grid that are not connected to the boundary of the grid. The key insight is to use a breadth-first search (BFS) approach to identify the connected land cells and mark them as visited.

**Approach**
1. Initialize a queue `q` to store the land cells that are connected to the boundary.
2. Iterate through the grid to find the land cells that are connected to the boundary. If a land cell is on the boundary, add it to the queue and mark it as visited.
3. Perform a BFS traversal from the land cells in the queue. For each visited land cell, mark its adjacent cells as visited and add them to the queue if they are not visited.
4. Continue the BFS traversal until the queue is empty.
5. The number of land cells that are not connected to the boundary is the number of land cells that were not visited during the BFS traversal.

**Time Complexity**
The time complexity of this solution is O(m*n), where m is the number of rows and n is the number of columns in the grid. This is because we iterate through the grid once to find the land cells connected to the boundary, and then perform a BFS traversal from these cells.

**Space Complexity**
The space complexity of this solution is also O(m*n), as in the worst case, we need to store all the land cells in the queue.

**Key Insight**
The key insight is to use a BFS approach to identify the connected land cells and mark them as visited. By doing so, we can efficiently count the number of land cells that are not connected to the boundary.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 78 ms (Beats 57.57%) |
| 💾 Memory | 19.6 MB (Beats 100%) |
| 📅 Solved | 2025-08-17 |
| 💻 Language | Python |