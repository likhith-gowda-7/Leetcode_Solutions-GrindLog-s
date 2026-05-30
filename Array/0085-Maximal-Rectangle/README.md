# 85. Maximal Rectangle


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximal-rectangle/)


## 📝 Problem Description

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return *its area*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)
```

**Input:** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
**Output:** 6
**Explanation:** The maximal rectangle is shown in the above picture.

```

Example 2:**

```

**Input:** matrix = [["0"]]
**Output:** 0

```

Example 3:**

```

**Input:** matrix = [["1"]]
**Output:** 1

```

 

**Constraints:**

	- `rows == matrix.length`

	- `cols == matrix[i].length`

	- `1 <= rows, cols <= 200`

	- `matrix[i][j]` is `'0'` or `'1'`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 23 ms (Beats 99.07%) |
| 💾 Memory | 24.8 MB (Beats 6.58%) |
| 📅 Solved | 2026-01-11 |
| 💻 Language | Python |