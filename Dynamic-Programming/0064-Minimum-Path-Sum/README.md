> 📌 **Cross-listed:** Primary location is [Array/0064-Minimum-Path-Sum](../../Array/0064-Minimum-Path-Sum). This problem also appears under: **Array**, **Dynamic Programming**, **Matrix**

# 64. Minimum Path Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-path-sum/)


## 📝 Problem Description

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)
```

**Input:** grid = [[1,3,1],[1,5,1],[4,2,1]]
**Output:** 7
**Explanation:** Because the path 1 &rarr; 3 &rarr; 1 &rarr; 1 &rarr; 1 minimizes the sum.

```

Example 2:**

```

**Input:** grid = [[1,2,3],[4,5,6]]
**Output:** 12

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 200`

	- `0 <= grid[i][j] <= 200`

## 🧠 Solution Explanation

## Intuition
The solution works by breaking down the problem into smaller sub-problems and storing the results of these sub-problems to avoid redundant computation. This approach is known as dynamic programming, which is particularly useful for problems that have overlapping sub-problems. By filling up a 2D table (`dp`) in a bottom-up manner, we can efficiently compute the minimum path sum.

## Approach
1. Initialize the first cell of the `dp` table with the value of the top-left cell of the `grid`.
2. Fill up the first row and first column of the `dp` table by adding the corresponding cell values from the `grid` to the previous cell values in the `dp` table.
3. For each remaining cell in the `dp` table, calculate the minimum path sum by adding the current cell value from the `grid` to the minimum of the cell values above and to the left in the `dp` table.
4. The minimum path sum is stored in the bottom-right cell of the `dp` table.

## Time Complexity
The time complexity is O(m*n), where m and n are the number of rows and columns in the `grid`, respectively. This is because we need to fill up the entire `dp` table, which has the same dimensions as the `grid`.

## Space Complexity
The space complexity is O(m*n), as we need to store the `dp` table, which has the same dimensions as the `grid`.

## Key Insight
The key insight is to recognize that the minimum path sum to a cell can be computed by considering only the minimum path sums to the cells above and to the left, which allows us to break down the problem into smaller sub-problems and solve them efficiently using dynamic programming.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 33.56%) |
| 💾 Memory | 20.2 MB (Beats 98.52%) |
| 📅 Solved | 2025-10-31 |
| 💻 Language | Python |