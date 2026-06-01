# 1128. Number of Equivalent Domino Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)


## 📝 Problem Description

Given a list of `dominoes`, `dominoes[i] = [a, b]` is **equivalent to** `dominoes[j] = [c, d]` if and only if either (`a == c` and `b == d`), or (`a == d` and `b == c`) - that is, one domino can be rotated to be equal to another domino.

Return *the number of pairs *`(i, j)`* for which *`0 <= i < j < dominoes.length`*, and *`dominoes[i]`* is **equivalent to** *`dominoes[j]`.

 

Example 1:**

```

**Input:** dominoes = [[1,2],[2,1],[3,4],[5,6]]
**Output:** 1

```

Example 2:**

```

**Input:** dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
**Output:** 3

```

 

**Constraints:**

	- `1 <= dominoes.length <= 4 * 10^4`

	- `dominoes[i].length == 2`

	- `1 <= dominoes[i][j] <= 9`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 8 ms (Beats 62.02%) |
| 💾 Memory | 24.3 MB (Beats 100%) |
| 📅 Solved | 2025-05-04 |
| 💻 Language | Python |