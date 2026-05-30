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

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.8 MB (Beats 28.25%) |
| 📅 Solved | 2026-03-04 |
| 💻 Language | Python |