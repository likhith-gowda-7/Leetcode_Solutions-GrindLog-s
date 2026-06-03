> 📌 **Cross-listed:** Primary location is [Array/0695-Max-Area-of-Island](../../Array/0695-Max-Area-of-Island). This problem also appears under: **Array**, **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Matrix**

# 695. Max Area of Island


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/max-area-of-island/)


## 📝 Problem Description

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return *the maximum **area** of an island in *`grid`. If there is no island, return `0`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)
```

**Input:** grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
**Output:** 6
**Explanation:** The answer is not 11, because the island must be connected 4-directionally.

```

Example 2:**

```

**Input:** grid = [[0,0,0,0,0,0,0,0]]
**Output:** 0

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 50`

	- `grid[i][j]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a Depth-First Search (DFS) approach to traverse the grid and calculate the area of each island. The key insight is that by marking visited cells as 0, we can avoid revisiting them and ensure that each island is counted only once.

**Approach**
1. Define a helper function `dfs` that takes a row and column as input and performs a DFS traversal from that cell.
2. Inside `dfs`, check if the current cell is out of bounds or is a 0 (water cell). If so, return immediately.
3. Increment the `count` variable to keep track of the current island's area.
4. Mark the current cell as visited by setting its value to 0.
5. Recursively call `dfs` on the neighboring cells (up, down, left, right).
6. In the main function, iterate over each cell in the grid. If the cell is a 1 (land cell), call `dfs` to calculate the area of the island.
7. Keep track of the maximum area found so far and return it at the end.

**Time Complexity**
O(m*n), where m is the number of rows and n is the number of columns in the grid. This is because we potentially visit each cell once during the DFS traversal.

**Space Complexity**
O(m*n), as we need to store the grid in memory. However, the space complexity of the DFS recursion is O(h), where h is the maximum height of the recursion stack. In the worst case, h = log(m*n), so the overall space complexity is O(m*n).

**Key Insight**
The key to this solution is the use of DFS to traverse the grid and mark visited cells as 0. This allows us to avoid revisiting cells and ensures that each island is counted only once. By keeping track of the maximum area found so far, we can efficiently find the maximum area of the island.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 85.7%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-08-09 |
| 💻 Language | Python |