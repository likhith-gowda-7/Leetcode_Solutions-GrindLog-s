> 📌 **Cross-listed:** Primary location is [Array/1582-Special-Positions-in-a-Binary-Matrix](../../Array/1582-Special-Positions-in-a-Binary-Matrix). This problem also appears under: **Array**, **Matrix**

# 1582. Special Positions in a Binary Matrix


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/special-positions-in-a-binary-matrix/)


## 📝 Problem Description

Given an `m x n` binary matrix `mat`, return *the number of special positions in *`mat`*.*

A position `(i, j)` is called **special** if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0` (rows and columns are **0-indexed**).

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/12/23/special1.jpg)
```

**Input:** mat = [[1,0,0],[0,0,1],[1,0,0]]
**Output:** 1
**Explanation:** (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg)
```

**Input:** mat = [[1,0,0],[0,1,0],[0,0,1]]
**Output:** 3
**Explanation:** (0, 0), (1, 1) and (2, 2) are special positions.

```

 

**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 100`

	- `mat[i][j]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution works by first counting the number of 1s in each row and column of the matrix. Then, it iterates through the matrix again to count the number of special positions, which are positions where the cell value is 1 and the row and column counts are both 1.

**Approach**
1. Initialize two arrays, `h1` and `h2`, of size `m` and `n` respectively, to keep track of the count of 1s in each row and column.
2. Iterate through the matrix, and for each cell with value 1, increment the corresponding count in `h1` and `h2`.
3. Initialize a counter `cnt` to keep track of the number of special positions.
4. Iterate through the matrix again, and for each cell with value 1, check if the row and column counts are both 1. If so, increment `cnt`.
5. Return the total count of special positions.

**Time Complexity**
O(m*n) because we are iterating through the matrix twice.

**Space Complexity**
O(m + n) because we are using two arrays of size `m` and `n` to store the row and column counts.

**Key Insight**
The key insight is that a position is special if and only if the cell value is 1 and the row and column counts are both 1. This allows us to count the special positions efficiently by first counting the row and column counts, and then iterating through the matrix again to count the special positions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.8 MB (Beats 28.06%) |
| 📅 Solved | 2026-03-04 |
| 💻 Language | Python |