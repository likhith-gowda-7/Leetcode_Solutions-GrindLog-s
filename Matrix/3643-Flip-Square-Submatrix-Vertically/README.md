> 📌 **Cross-listed:** Primary location is [Array/3643-Flip-Square-Submatrix-Vertically](../../Array/3643-Flip-Square-Submatrix-Vertically). This problem also appears under: **Array**, **Two Pointers**, **Matrix**

# 3643. Flip Square Submatrix Vertically


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/flip-square-submatrix-vertically/)


## 📝 Problem Description

You are given an `m x n` integer matrix `grid`, and three integers `x`, `y`, and `k`.

The integers `x` and `y` represent the row and column indices of the **top-left** corner of a **square** submatrix and the integer `k` represents the size (side length) of the square submatrix.

Your task is to flip the submatrix by reversing the order of its rows vertically.

Return the updated matrix.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2025/07/20/gridexmdrawio.png)

**Input:** grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3

**Output:** [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]

**Explanation:**

The diagram above shows the grid before and after the transformation.

Example 2:**

![](https://assets.leetcode.com/uploads/2025/07/20/gridexm2drawio.png)​​​​​​​

**Input:** grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2

**Output:** [[3,4,4,2],[2,3,2,3]]

**Explanation:**

The diagram above shows the grid before and after the transformation.

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 50`

	- `1 <= grid[i][j] <= 100`

	- `0 <= x < m`

	- `0 <= y < n`

	- `1 <= k <= min(m - x, n - y)`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 67.07%) |
| 📅 Solved | 2026-03-21 |
| 💻 Language | Python |