# 931. Minimum Falling Path Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/)


## 📝 Problem Description

Given an `n x n` array of integers `matrix`, return *the **minimum sum** of any **falling path** through* `matrix`.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)
```

**Input:** matrix = [[2,1,3],[6,5,4],[7,8,9]]
**Output:** 13
**Explanation:** There are two falling paths with a minimum sum as shown.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg)
```

**Input:** matrix = [[-19,57],[-40,-5]]
**Output:** -59
**Explanation:** The falling path with a minimum sum is shown.

```

 

**Constraints:**

	- `n == matrix.length == matrix[i].length`

	- `1 <= n <= 100`

	- `-100 <= matrix[i][j] <= 100`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 31 ms (Beats 32.98%) |
| 💾 Memory | 18.9 MB (Beats 100%) |
| 📅 Solved | 2025-11-11 |
| 💻 Language | Python |