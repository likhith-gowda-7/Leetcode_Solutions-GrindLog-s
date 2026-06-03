# 200. Number of Islands


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-islands/)


## 📝 Problem Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:**

```

**Input:** grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
**Output:** 1

```

Example 2:**

```

**Input:** grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
**Output:** 3

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 300`

	- `grid[i][j]` is `'0'` or `'1'`.

## 🧠 Solution Explanation

## Intuition
The solution works by iterating over each cell in the grid and using a depth-first search (DFS) to mark all connected land cells as visited. This approach effectively groups all cells in an island together, allowing us to count the number of distinct islands. By modifying the grid in-place to mark visited cells, we avoid revisiting the same island multiple times.

## Approach
1. Initialize variables to store the number of rows (`m`) and columns (`n`) in the grid.
2. Define a nested DFS function that takes a row and column as input and recursively explores all adjacent land cells.
3. Iterate over each cell in the grid, and when a land cell is encountered, call the DFS function to mark all connected land cells as visited and increment the island count.
4. Return the total count of islands found.

## Time Complexity
The time complexity is O(m*n), where `m` and `n` are the number of rows and columns in the grid, respectively. This is because in the worst-case scenario, we might need to visit every cell in the grid.

## Space Complexity
The space complexity is O(m*n), which is used by the recursive call stack in the worst-case scenario (when the grid is filled with lands and the DFS goes by m*n deep).

## Key Insight
The key insight is to use DFS to group connected land cells together, allowing us to count the number of distinct islands by incrementing a counter each time we encounter a new, unvisited land cell. This approach takes advantage of the fact that islands are defined as connected components in the grid.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 233 ms (Beats 86.26%) |
| 💾 Memory | 19.9 MB (Beats 100%) |
| 📅 Solved | 2025-08-08 |
| 💻 Language | Python |