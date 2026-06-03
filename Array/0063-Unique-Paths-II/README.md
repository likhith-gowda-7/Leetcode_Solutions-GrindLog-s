# 63. Unique Paths II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/unique-paths-ii/)


## 📝 Problem Description

You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)
```

**Input:** obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
**Output:** 2
**Explanation:** There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)
```

**Input:** obstacleGrid = [[0,1],[0,0]]
**Output:** 1

```

 

**Constraints:**

	- `m == obstacleGrid.length`

	- `n == obstacleGrid[i].length`

	- `1 <= m, n <= 100`

	- `obstacleGrid[i][j]` is `0` or `1`.

## 🧠 Solution Explanation

## Intuition
This solution works by using a top-down dynamic programming (DP) approach to calculate the number of unique paths to the bottom-right corner. The key idea is to break down the problem into smaller sub-problems and store the results of these sub-problems to avoid redundant calculations. The presence of obstacles in the grid is handled by checking if the current cell is an obstacle and returning 0 if it is.

## Approach
1. Check if the goal cell (bottom-right corner) is an obstacle. If it is, return 0 because there's no way to reach it.
2. Initialize a memoization dictionary with the base case, which is the goal cell itself.
3. Define a recursive function `dfs` that takes the current row and column as parameters.
4. In the `dfs` function, check if the current cell is out of bounds or an obstacle. If it is, return 0.
5. If the current cell is not in the memoization dictionary, calculate the number of unique paths to it by recursively calling `dfs` for the cell below and the cell to the right, and store the result in the dictionary.
6. Return the number of unique paths to the current cell.

## Time Complexity
The time complexity is O(m*n), where m and n are the number of rows and columns in the grid, respectively. This is because each cell is visited at most once and the recursive function calls are memoized to avoid redundant calculations.

## Space Complexity
The space complexity is also O(m*n), which is used to store the memoization dictionary. In the worst-case scenario, the dictionary will store a value for each cell in the grid.

## Key Insight
The key insight here is to use memoization to store the results of sub-problems and avoid redundant calculations. This approach allows the solution to efficiently handle grids with obstacles and calculate the number of unique paths to the bottom-right corner.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-10-26 |
| 💻 Language | Python |