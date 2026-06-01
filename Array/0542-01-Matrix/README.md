# 542. 01 Matrix


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/01-matrix/)


## 📝 Problem Description

Given an `m x n` binary matrix `mat`, return *the distance of the nearest *`0`* for each cell*.

The distance between two cells sharing a common edge is `1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)
```

**Input:** mat = [[0,0,0],[0,1,0],[0,0,0]]
**Output:** [[0,0,0],[0,1,0],[0,0,0]]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)
```

**Input:** mat = [[0,0,0],[0,1,0],[1,1,1]]
**Output:** [[0,0,0],[0,1,0],[1,2,1]]

```

 

**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 10^4`

	- `1 <= m * n <= 10^4`

	- `mat[i][j]` is either `0` or `1`.

	- There is at least one `0` in `mat`.

 

**Note:** This question is the same as 1765: [https://leetcode.com/problems/map-of-highest-peak/](https://leetcode.com/problems/map-of-highest-peak/description/)

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 127 ms (Beats 46.48%) |
| 💾 Memory | 20.5 MB (Beats 99.96%) |
| 📅 Solved | 2025-08-14 |
| 💻 Language | Python |