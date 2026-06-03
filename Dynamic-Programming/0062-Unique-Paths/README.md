> 📌 **Cross-listed:** Primary location is [Math/0062-Unique-Paths](../../Math/0062-Unique-Paths). This problem also appears under: **Math**, **Dynamic Programming**, **Combinatorics**

# 62. Unique Paths


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Combinatorics](https://img.shields.io/badge/Combinatorics-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/unique-paths/)


## 📝 Problem Description

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
```

**Input:** m = 3, n = 7
**Output:** 28

```

Example 2:**

```

**Input:** m = 3, n = 2
**Output:** 3
**Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

```

 

**Constraints:**

	- `1 <= m, n <= 100`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using dynamic programming by breaking it down into smaller sub-problems. The key insight is that each cell in the grid can be reached from the cell above it or the cell to its left, and the number of ways to reach a cell is the sum of the number of ways to reach the cell above it and the cell to its left.

**Approach**
1. Initialize a 2D array `dp` to store the number of unique paths to reach each cell.
2. If the current cell is at the top or left edge of the grid, there is only one way to reach it (i.e., by moving from the top-left corner).
3. For all other cells, the number of unique paths to reach the cell is the sum of the number of unique paths to reach the cell above it and the cell to its left.
4. Return the value of the bottom-right cell in the `dp` array.

**Time Complexity**
O(m*n), where m and n are the dimensions of the grid. This is because we need to iterate over each cell in the grid once to fill up the `dp` array.

**Space Complexity**
O(m*n), where m and n are the dimensions of the grid. This is because we need to store the number of unique paths to reach each cell in the `dp` array.

**Key Insight**
The key insight is that the number of unique paths to reach a cell is the sum of the number of unique paths to reach the cell above it and the cell to its left. This is because the robot can only move down or right, so the number of ways to reach a cell is the sum of the number of ways to reach the cell above it and the cell to its left.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-10-24 |
| 💻 Language | Python |