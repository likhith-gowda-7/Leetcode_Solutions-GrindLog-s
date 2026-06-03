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

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the rows of the square submatrix and swapping the elements at the top and bottom row indices for each column. This effectively reverses the order of the rows vertically.

**Approach**
1. Calculate the row indices of the top and bottom row of the square submatrix (`l` and `r`).
2. Iterate through the columns of the square submatrix, swapping the elements at the top and bottom row indices for each column.
3. Move the row indices towards the center of the submatrix (`l` increments and `r` decrements).
4. Repeat steps 2-3 until the top and bottom row indices meet or cross.
5. Return the updated matrix.

**Time Complexity**
O(n*k), where n is the number of columns in the matrix and k is the size of the square submatrix. This is because we iterate through each column of the submatrix once.

**Space Complexity**
O(1), as we only modify the existing matrix in-place and do not allocate any additional space.

**Key Insight**
The key insight is to recognize that we only need to swap the elements at the top and bottom row indices for each column, rather than reversing the entire row. This allows us to iterate through the columns in a single pass, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 67.07%) |
| 📅 Solved | 2026-03-21 |
| 💻 Language | Python |